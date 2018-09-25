// access all six of the nav buttons
var buttons = document.getElementById("siteNav").children

for (var i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener("click", function() {
    this.classList.add("active")
  })
}
