import json

def load_units():
    with open("data/units.json") as f:
        return json.load(f)