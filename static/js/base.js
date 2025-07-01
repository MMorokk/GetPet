let darkmode = localStorage.getItem("darkmode");
const themeSwitch = document.getElementById("theme-switch");
const navbar = document.querySelector("header");
const openButton = document.getElementById("open-sidebar-button");
const media = window.matchMedia(
  "screen and (max-width: 700px), screen and (max-device-width: 700px)"
);

const enableDarkmode = () => {
  document.body.classList.add("darkmode");
  localStorage.setItem("darkmode", "active");
};

const disableDarkmode = () => {
  document.body.classList.remove("darkmode");
  localStorage.setItem("darkmode", null);
};

themeSwitch.addEventListener("click", () => {
  darkmode = localStorage.getItem("darkmode");
  darkmode !== "active" ? enableDarkmode() : disableDarkmode();
});

if (
  darkmode == "active" ||
  (window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches)
) {
  enableDarkmode();
} else {
  disableDarkmode();
}

function openSidebar() {
  navbar.classList.add("show");
  openButton.setAttribute("aria-expanded", "true");
  navbar.removeAttribute("inert");
}

function closeSidebar() {
  if (media.matches) {
    navbar.classList.remove("show");
    openButton.setAttribute("aria-expanded", "false");
    navbar.setAttribute("inert", "");
  }
}

media.addEventListener("change", (e) => updateNavbar(e));

function updateNavbar(e) {
  const isMobile = e.matches;
  if (isMobile) {
    navbar.setAttribute("inert", "");
  } else {
    navbar.removeAttribute("inert");
  }
}

updateNavbar(media);

const navLinks = document.querySelectorAll("nav a");
navLinks.forEach((link) => {
  link.addEventListener("click", () => {
    closeSidebar();
  });
});
