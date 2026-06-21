import time
from loader import load_units, create_character
from runner import run_simulation

units = load_units()


team1 = [create_character(units, "Reksai", 1),
         create_character(units, "Reksai", 3)
         ]

team2 = [create_character(units, "Aatrox", 2),
         create_character(units, "Aatrox", 2)
         ]

start_time = time.perf_counter()
wins, avg_time = run_simulation(team1, team2, 1000)
end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Tempo de exucução: {execution_time:.2f}s")

print(wins)
print(f"Tempo médio do combate: {avg_time:.2f}s")