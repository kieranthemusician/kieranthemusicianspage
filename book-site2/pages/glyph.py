import cv2
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

OUTPUT_DIR = "accepted_letters"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def segment_letters(binary_word):
    h, w = binary_word.shape
    proj = binary_word.sum(axis=0)
    proj = proj / proj.max()

    cuts = []
    for i in range(1, w - 1):
        if proj[i] < 0.15 and proj[i - 1] >= 0.15:
            cuts.append(i)

    letters = []
    prev = 0
    for c in cuts + [w]:
        if c - prev > 8:
            letters.append(binary_word[:, prev:c])
        prev = c

    return letters


class LetterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackletter Letter Extractor")

        self.letters = []
        self.index = 0

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 16), width=10)
        self.entry.pack()

        btns = tk.Frame(root)
        btns.pack(pady=5)

        tk.Button(btns, text="GOOD", width=10,
                  command=self.save_good).pack(side="left", padx=5)
        tk.Button(btns, text="BAD", width=10,
                  command=self.skip_bad).pack(side="left", padx=5)

        tk.Button(root, text="Open Page",
                  command=self.load_image).pack(pady=5)

    def load_image(self):
        path = filedialog.askopenfilename()
        if not path:
            return

        gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        _, binary = cv2.threshold(
            gray, 180, 255, cv2.THRESH_BINARY_INV
        )

        contours, _ = cv2.findContours(
            binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        self.letters = []

        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            if h < 40 or w < 60:
                continue

            word = binary[y:y + h, x:x + w]
            letter_imgs = segment_letters(word)

            for l in letter_imgs:
                if l.shape[1] < 8:
                    continue
                l = cv2.resize(
                    l, None, fx=4, fy=4,
                    interpolation=cv2.INTER_CUBIC
                )
                self.letters.append(l)

        self.index = 0
        self.show_letter()

    def show_letter(self):
        if self.index >= len(self.letters):
            self.image_label.config(text="DONE")
            return

        img = Image.fromarray(255 - self.letters[self.index])
        img = img.convert("L")
        tk_img = ImageTk.PhotoImage(img)
        self.image_label.image = tk_img
        self.image_label.config(image=tk_img)
        self.entry.delete(0, tk.END)

    def save_good(self):
        label = self.entry.get().strip()
        if not label:
            return

        fname = f"{label}_{self.index}.png"
        cv2.imwrite(
            os.path.join(OUTPUT_DIR, fname),
            self.letters[self.index]
        )

        self.index += 1
        self.show_letter()

    def skip_bad(self):
        self.index += 1
        self.show_letter()


root = tk.Tk()
app = LetterGUI(root)
root.mainloop()
