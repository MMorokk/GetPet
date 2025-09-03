const themeSwitch = document.getElementById("theme-switch");

const enableDarkmode = () => {
  document.body.classList.add("darkmode");
  localStorage.setItem("darkmode", "active");
};

const disableDarkmode = () => {
  document.body.classList.remove("darkmode");
  localStorage.setItem("darkmode", "inactive"); // or use removeItem("darkmode") to let OS preference apply
};

if (themeSwitch) {
  themeSwitch.addEventListener("click", () => {
    const isDark = document.body.classList.toggle("darkmode");
    localStorage.setItem("darkmode", isDark ? "active" : "inactive");
  });
}

// Initialization: prefer stored choice, otherwise fall back to OS preference
const stored = localStorage.getItem("darkmode");
const prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;

if (stored === "active" || (stored === null && prefersDark)) {
  enableDarkmode();
} else {
  disableDarkmode();
}
