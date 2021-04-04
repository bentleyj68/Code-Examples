from flask import Flask, jsonify

justice_league_members = [
    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
    {"superhero": "Batman", "real_name": "Bruce Wayne"},
    {"superhero": "Cyborg", "real_name": "Victor Stone"},
    {"superhero": "Flash", "real_name": "Barry Allen"},
    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
    {"superhero": "Superman", "real_name": "Clark Kent/Kal-El"},
    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
]

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/justice-league")
def justice_league():
    """Return the justice league data as json"""

    return jsonify(justice_league_members)


@app.route("/")
def welcome():
    return (
        f"Welcome to the Justice League API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/justice-league<br/>"
        f"/api/v1.0/justice-league/superhero/aquaman"
        f"/api/v1.0/justice-league/superhero/batman"
        f"/api/v1.0/justice-league/superhero/cyborg"
        f"/api/v1.0/justice-league/superhero/flash"
        f"/api/v1.0/justice-league/superhero/green%20lantern"
        f"/api/v1.0/justice-league/superhero/superman"
        f"/api/v1.0/justice-league/superhero/wonder%20woman"
    )

@app.route("/api/v1.0/justice-league/<super_name>")
def justice_league_character(super_name):
    """Fetch the Justice League character whose super hero name matches
       the path variable supplied by the user, or a 404 if not."""

    canonicalized = super_name.replace(" ", "").lower()
    for character in justice_league_members:
        search_term = character["superhero"].replace(" ", "").lower()

        if search_term == canonicalized:
            return jsonify(character)

    # return jsonify({"error": f"Character with superhero {super_name} not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)
