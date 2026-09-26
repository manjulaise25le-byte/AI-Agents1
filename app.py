from flask import Flask, render_template, request

app = Flask(__name__)


# ==============================
# TRAVEL AGENT TOOLS
# ==============================

def search_transport(source, destination):
    return {
        "type": "Bus",
        "price": 1200,
        "duration": "10 hours"
    }


def search_hotel(destination):
    return {
        "name": "Beach View Hotel",
        "price_per_day": 2500,
        "location": "Near Beach"
    }


def check_weather(destination):
    return {
        "condition": "Sunny",
        "temperature": "29°C"
    }


# ==============================
# HOME PAGE
# ==============================

@app.route("/")
def home():
    return render_template("index.html")


# ==============================
# PLAN TRIP
# ==============================

@app.route("/plan", methods=["POST"])
def plan_trip():

    source = request.form["source"]
    destination = request.form["destination"]
    days = int(request.form["days"])
    budget = float(request.form["budget"])

    # Search transportation
    transport = search_transport(
        source,
        destination
    )

    # Search hotel
    hotel = search_hotel(destination)

    # Check weather
    weather = check_weather(destination)

    # Calculate costs
    transport_cost = transport["price"]

    hotel_cost = (
        hotel["price_per_day"] * days
    )

    total_cost = transport_cost + hotel_cost

    # Re-planning
    replanned = False

    if total_cost > budget:

        replanned = True

        hotel["name"] = "Budget Beach Hotel"
        hotel["price_per_day"] = 1800

        hotel_cost = (
            hotel["price_per_day"] * days
        )

        total_cost = transport_cost + hotel_cost

    return render_template(
        "index.html",
        result=True,
        source=source,
        destination=destination,
        days=days,
        budget=budget,
        transport=transport,
        hotel=hotel,
        weather=weather,
        transport_cost=transport_cost,
        hotel_cost=hotel_cost,
        total_cost=total_cost,
        replanned=replanned
    )


# ==============================
# RUN APPLICATION
# ==============================

if __name__ == "__main__":
    app.run(debug=True)