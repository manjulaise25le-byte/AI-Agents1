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
        "price": 2500,
        "rating": "4.5/5"
    }


def create_itinerary(source, destination, days):
    return [
        f"Day 1: Travel from {source} to {destination}",
        f"Day 2: Visit famous places in {destination}",
        f"Day 3: Enjoy local food and sightseeing in {destination}",
        f"Day {days}: Return journey"
    ]


# ==============================
# HOME PAGE
# ==============================

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        source = request.form["source"]
        destination = request.form["destination"]
        days = int(request.form["days"])

        transport = search_transport(source, destination)
        hotel = search_hotel(destination)
        itinerary = create_itinerary(source, destination, days)

        result = {
            "source": source,
            "destination": destination,
            "days": days,
            "transport": transport,
            "hotel": hotel,
            "itinerary": itinerary
        }

    return render_template("index.html", result=result)


# ==============================
# RUN APPLICATION
# ==============================

if __name__ == "__main__":
    app.run(debug=True)