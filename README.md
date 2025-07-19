# Social-Food-Delivery-App
This is a simple example of a social food delivery application. It demonstrates a minimal backend written in Python using the [Flask](https://flask.palletsprojects.com/) framework.

The application exposes a few basic endpoints to retrieve restaurants, view menu items, and place orders. The purpose is to provide a small reference implementation with well-commented code that you can build upon.

## Getting Started

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**

   ```bash
   python app.py
   ```

   The server will start on `http://127.0.0.1:5000/`.

3. **Try the endpoints**

   - `GET /restaurants` &ndash; list available restaurants
   - `GET /restaurants/<id>` &ndash; retrieve a single restaurant by ID
   - `POST /orders` &ndash; place an order (sample payload in `app.py`)

This is intentionally lightweight so you can customize and expand it for your own needs. Enjoy exploring the code!
