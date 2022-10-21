function reverseNumber() {
  let x = document.getElementById("number").value;
  let array = x.toString().split("");
  let rev = "";
  for (let i = array.length - 1; i >= 0; i--) {
    rev += array[i];
  }
  document.getElementById("f1").innerHTML = "1. " + rev;
}

function addEven() {
  let x = document.getElementById("number").value;
  let array = x.toString().split("");
  let sum = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] % 2 === 0) {
      sum += parseInt(array[i]);
    }
  }
  document.getElementById("f2").innerHTML = "2. " + sum;
}
