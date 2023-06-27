function validateForm() {
    var toppings = document.forms["pizza_form"]["toppings"].value;
    var extra_cheese_no = document.getElementById('no_yes').checked
    var extra_cheese_yes = document.getElementById('yes_no').checked
    var time = document.forms["pizza_form"]["time"].value;

    if (toppings == "") {
      alert("Name must be filled out");
      return false;
    }
    if (!extra_cheese_no && !extra_cheese_yes) {
        alert("Extra cheese must be filled out");
        return false;
      }
    if (!moment(time, 'HH:mm', true).isValid()) {
        alert("Time must be filled out");
        return false;
    }
    return true;
  }