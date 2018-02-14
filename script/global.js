const para = document.getElementsByClassName("parallax-container")[0];

document.body.onscroll = function () {
  para.scrollTop = window.pageYOffset || document.documentElement.scrollTop;
};