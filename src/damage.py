def apply_damage(damage, defender, damage_type):

    if damage_type == "physical":
        reduction = defender.armor/(defender.armor + 100)

    elif damage_type == "magic":
        reduction = defender.magic_resist/(defender.magic_resist + 100)

    else:
        reduction = 0  # true damage no futuro

    final_damage = damage*(1 - reduction)

    return max(1, int(final_damage))