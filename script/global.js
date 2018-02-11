const para = document.getElementsByClassName("paralax-container")[0];

document.body.onscroll = function() {
   // if(document.body.scrollHeight <= para.scrollHeight / 2){
        para.scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    //}
  };
