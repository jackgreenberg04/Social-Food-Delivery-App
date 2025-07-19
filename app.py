"""Simple Social Food Delivery backend using Flask.

This example illustrates a minimal web API for a fictional food
ordering application. Everything is stored in memory so it is easy
to understand without a database. The endpoints are just samples that
show how you might structure a larger project.
"""

from flask import Flask, jsonify, request

# Create the Flask application instance.  This object handles routing
# and dispatching incoming HTTP requests to the view functions defined
# below.
app = Flask(__name__)

# ---------------------------------------------------------------------------
# Data models (in memory for simplicity)
# ---------------------------------------------------------------------------
# Normally you would store this in a proper database.  For a short example
# we just keep the data in plain Python lists so you can see how everything
# fits together without any extra setup.

# A list of restaurants with a simple menu for each one.
restaurants = [
    {
        "id": 1,
        "name": "Pizza Palace",
        "menu": ["Margherita", "Pepperoni", "Veggie"],
    },
    {
        "id": 2,
        "name": "Sushi Central",
        "menu": ["California Roll", "Spicy Tuna", "Salmon Nigiri"],
    },
]

# A list to keep track of orders that are placed.
orders = []

# ---------------------------------------------------------------------------
# Routes / Endpoints
# ---------------------------------------------------------------------------

@app.route("/restaurants", methods=["GET"])
def list_restaurants():
    """Return a list of all available restaurants."""
    return jsonify(restaurants)


@app.route("/restaurants/<int:restaurant_id>", methods=["GET"])
def get_restaurant(restaurant_id):
    """Retrieve a single restaurant by its ID.

    If the restaurant does not exist we return a 404 error.
    """
    for r in restaurants:
        if r["id"] == restaurant_id:
            return jsonify(r)
    return jsonify({"error": "Restaurant not found"}), 404


@app.route("/orders", methods=["POST"])
def place_order():
    """Place an order for one of the restaurants.

    The request is expected to contain JSON with `restaurant_id` and a list
    of `items`. Example:

    ```json
    {
      "restaurant_id": 1,
      "items": ["Margherita", "Pepperoni"]
    }
    ```
    """
    data = request.get_json()

    # Basic validation of the incoming payload.
    if not data or "restaurant_id" not in data or "items" not in data:
        return jsonify({"error": "Invalid order format"}), 400

    # In a real application you would also check that the restaurant exists
    # and that the requested menu items are valid.
    orders.append(data)
    return jsonify({"status": "Order received", "order": data}), 201


if __name__ == "__main__":
    # When running this file directly (`python app.py`), start the development
    # server. `debug=True` gives helpful error messages.
    app.run(debug=True)
