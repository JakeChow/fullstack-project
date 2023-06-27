import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="Pizza">
        <p>Papa's Pizzeria</p>
      </header>
      <div>
        <form name="pizza_form" action="/Pizza_page.php" onsubmit="return validateForm()">
          <div>
            <label for="toppings">Toppings:</label>
            <input type="text" id="toppings" name="pizza_toppings" maxlength="100"></input>
          </div>
          <div>
            <label for="yes_no_radio">Extra Cheese:</label>
            <input type="radio" id="yes_no" name="extra_cheese" value="Yes" />
            <label for="yes_no">Yes</label>
            <input type="radio" id="no_yes" name="extra_cheese" value="No" />
            <label for="no_yes">No</label>
          </div>
          <div>
            <label for="date">Date of delivery:</label>
            <input name="date" id="date" type="date" min="2023-06-20"></input>
          </div>
          <div>
            <label for="date">Time of delivery:</label>
            <input name="time" id="time" type="time"></input>
          </div>
          <div>
            <label for="delivery_instructions">Delivery Instructions::</label>
            <input
              type="text"
              id="delivery_instructions"
              name="deliver_instr"
              maxlength="100"
            ></input>
          </div>
          <input type="submit" value="Submit"></input>
        </form>
      </div>
      <footer>
        <p>
          <a href="pizzahut.com">papaspizza.com</a>
        </p>
      </footer>
      <script src="validate.js"></script>
    </div>
  );
}

export default App;
