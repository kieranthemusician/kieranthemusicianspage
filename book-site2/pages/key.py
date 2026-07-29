from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register blackletter font
pdfmetrics.registerFont(
    TTFont("Blackletter", "UnifrakturCook-Bold.ttf")
)

file_path = "1500s_English_Blackletter_Letter_Key.pdf"
c = canvas.Canvas(file_path, pagesize=letter)
width, height = letter

# Title
c.setFont("Times-Bold", 26)
c.drawCentredString(width / 2, height - 50,
                    "1500s English Blackletter Letter Key")

y = height - 100

pairs = [
    ("𝔄","A"),("𝔅","B"),("ℭ","C"),("𝔇","D"),("𝔈","E"),
    ("𝔉","F"),("𝔊","G"),("ℌ","H"),("ℑ","I"),("𝔍","J"),
    ("𝔎","K"),("𝔏","L"),("𝔐","M"),("𝔑","N"),("𝔒","O"),
    ("𝔓","P"),("𝔔","Q"),("ℜ","R"),("𝔖","S"),("𝔗","T"),
    ("𝔘","U"),("𝔙","V"),("𝔚","W"),("𝔛","X"),("𝔜","Y"),
    ("ℨ","Z"),

    ("𝔞","a"),("𝔟","b"),("𝔠","c"),("𝔡","d"),("𝔢","e"),
    ("𝔣","f"),("𝔤","g"),("𝔥","h"),("𝔦","i"),("𝔧","j"),
    ("𝔨","k"),("𝔩","l"),("𝔪","m"),("𝔫","n"),("𝔬","o"),
    ("𝔭","p"),("𝔮","q"),("𝔯","r"),("ſ","s"),("𝔱","t"),
    ("𝔲","u"),("𝔳","v"),("𝔴","w"),("𝔵","x"),("𝔶","y"),
    ("𝔷","z"),

    ("þ","th"),("ȝ","y / gh"),("ꝛ","r")
]

for orig, modern in pairs:
    if y < 80:
        c.showPage()
        y = height - 80

    c.setFont("Blackletter", 44)
    c.drawString(80, y, orig)

    c.setFont("Times-Roman", 20)
    c.drawString(160, y + 10, f"→ {modern}")

    y -= 46

c.save()
print("PDF created successfully.")
