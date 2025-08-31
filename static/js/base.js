const navbar = document.querySelector("header");
const openButton = document.getElementById("open-sidebar-button");
const media = window.matchMedia(
  "screen and (max-width: 700px), screen and (max-device-width: 700px)"
);

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
