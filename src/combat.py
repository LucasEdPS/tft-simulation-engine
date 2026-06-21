import random
from damage import apply_damage

def fight(team1, team2):

    # reset
    for unit in team1 + team2:
        unit.reset()
        unit.attack_cooldown = (10 / unit.attack_speed)
        unit.next_attack_time = 0

    current_time = 0

    # loop principal
    while team1 and team2:

        all_units = [u for u in team1 + team2 if u.is_alive()]

        pending_attacks = []

        for attacker in all_units:

            # só age quando chega o tempo dele
            if current_time <= attacker.next_attack_time:
                continue

            # definir inimigos
            enemies = team2 if attacker in team1 else team1
            enemies = [e for e in enemies if e.is_alive()]

            if not enemies:
                continue

            defender = random.choice(enemies)

            # AUTO ATTACK
            damage = apply_damage(attacker.attack, defender, "physical")
            pending_attacks.append((defender, damage))

            # próximo ataque
            attacker.next_attack_time = current_time + attacker.attack_cooldown

        for defender, damage in pending_attacks:
                defender.take_damage(damage)

        # limpar mortos
        team1 = [u for u in team1 if u.is_alive()]
        team2 = [u for u in team2 if u.is_alive()]

        # avançar tempo
        current_time += 1

    if not team1 and not team2:
        winner = "draw"
    elif team1:
        winner = "team1"
    else:
        winner = "team2"
    
    combat_time_seconds = current_time / 10

    return winner, combat_time_seconds