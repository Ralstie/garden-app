# Garden Advice Program
# Provides gardening advice based on the season and plant type.


def get_season_advice(season):
    """Return gardening advice based on the season."""
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """Return gardening advice based on the type of plant."""
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def generate_advice(season, plant_type):
    """Generate combined gardening advice."""
    advice = get_season_advice(season)
    advice += get_plant_advice(plant_type)
    return advice


# Current season and plant type.
season = "summer"
plant_type = "flower"

# Generate and display the gardening advice.
advice = generate_advice(season, plant_type)
print(advice)