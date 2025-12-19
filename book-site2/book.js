const PAGE_COUNT = 1120; // ← change to your actual page count
const PAD = 4;

const PAGE_WIDTH = 1200;
const PAGE_HEIGHT = 1800;

function page(n) {
  const num = String(n).padStart(PAD, "0");
  return {
    uri: `pages/page-${num}.jpg`,
    width: PAGE_WIDTH,
    height: PAGE_HEIGHT
  };
}

const data = [];

// First page alone
data.push([page(1)]);

// Two-page spreads
for (let i = 2; i <= PAGE_COUNT; i += 2) {
  const left = page(i);
  const right = (i + 1 <= PAGE_COUNT) ? page(i + 1) : null;
  data.push(right ? [left, right] : [left]);
}

const br = new BookReader({
  data,
  bookTitle: "Original Matthew Bible from 1537",
  imagesBaseURL:
    "https://cdn.jsdelivr.net/npm/@internetarchive/bookreader@5.0.0-87/BookReader/images/",
  ui: "full",
  el: "#BookReader"
});

br.init();

if (!location.hash) {
  location.hash = "#mode/2up";
}
