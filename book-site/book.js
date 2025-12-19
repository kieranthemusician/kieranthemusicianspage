// TOTAL number of pages (must match your images)
const PAGE_COUNT = 556; // ← change if needed

const PAGE_WIDTH = 1200;
const PAGE_HEIGHT = 1800;
const PAD = 4; // because page-0001.jpg

function page(n) {
  const num = String(n).padStart(PAD, "0");
  return {
    uri: `pages/page-${num}.jpg`,
    width: PAGE_WIDTH,
    height: PAGE_HEIGHT
  };
}

const data = [];

// Cover page alone
data.push([page(1)]);

// Two-page spreads
for (let i = 2; i <= PAGE_COUNT; i += 2) {
  const left = page(i);
  const right = (i + 1 <= PAGE_COUNT) ? page(i + 1) : null;
  data.push(right ? [left, right] : [left]);
}

const br = new BookReader({
  data,
  bookTitle: "Praise Jesus Christ, the King of Kings",
  imagesBaseURL:
    "https://cdn.jsdelivr.net/npm/@internetarchive/bookreader@5.0.0-87/BookReader/images/",
  ui: "full",
  el: "#BookReader"
});

br.init();

// Start immediately in book (two-page) mode
if (!location.hash) {
  location.hash = "#mode/2up";
}
