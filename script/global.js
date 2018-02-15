document.addEventListener('scroll', function () {
    let para = document.getElementsByClassName("parallax-container")[0];
    let scroll = window.pageYOffset || document.documentElement.scrollTop;
    if (scroll <= para.scrollHeight) {
        para.scrollTop = scroll;
    }
});

function supportsFocusWithin() {
    try {
        let ss = document.styleSheets[0]
        ss.insertRule('html:focus-within', 0);
        ss.deleteRule(0);
        return true;
    } catch (e) {
        return false;
    }
}

function focusClass(e, f) {
    e.cancelBubble = true;
    if (typeof e.srcElement !== 'undefined' && e.srcElement !== null) {
        let p = e.srcElement.closest("ul");
        if (p.classList.contains("nav-flyout")) {
            f ? p.classList.add("nav-focus") : p.classList.remove("nav-focus");
        }
    }
}

document.addEventListener('DOMContentLoaded', function () {
    if (!supportsFocusWithin()) {
        document.addEventListener('blur', function (e) {
            focusClass(e, false);
        }, true);
        document.addEventListener('focus', function (e) {
            focusClass(e, true);
        }, true);
    }
});