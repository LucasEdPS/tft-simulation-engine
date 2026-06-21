from combat import fight

def run_simulation(team1, team2, n):

    wins = {"team1": 0, "team2": 0, "draw":0}
    total_time = 0

    for _ in range(n):
        result, fight_time = fight(team1, team2)

        wins[result] += 1
        total_time += fight_time

    avg_time = total_time / n

    return wins, avg_time