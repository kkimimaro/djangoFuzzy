var i = 0;
var original = document.getElementById('selectorSquad');

function duplicate() {
    var clone = original.cloneNode(true); // "deep" clone
    i = i + 1

    clone.id = "selectorSquad" + i;
    clone.setAttribute('name', clone.id)
    clone.style.setProperty('display', "flex");
    clone.style.setProperty('justify-content', "space-between");
    clone.style.setProperty('margin-top', "10px");

    original.parentElement.appendChild(clone);
    for (let j = 0; j < clone.children.length; j++) {
    var currentChildren = clone.children[j]
      currentChildren.setAttribute('name', currentChildren.getAttribute('name') + i);
    }

    document.getElementById('amount').value = i+1;
}