import json
from character import Character

def load_units():
    with open("data/units.json") as f:
        return json.load(f)

def create_character(units, name, star):
    data = units[name]["stats"][str(star)]
    unit_data = units[name]

    char = Character(
        name=f"{name}_{star}",
        base_name=name,
        star=star,
        hp=data["hp"],
        attack=data["attack"],
        armor=data["armor"],
        magic_resist=data["magic_resist"],
        attack_speed=data["attack_speed"],
        mana_initial=data["mana_initial"],
        mana_max=data["mana_max"],
        range_ =unit_data["range"]
    )
    return char