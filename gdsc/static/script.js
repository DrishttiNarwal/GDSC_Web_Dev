function loadAboutContent() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "about.html", true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            document.getElementById("aboutContent").innerHTML = xhr.responseText;
        }
    };
    xhr.send();
}
