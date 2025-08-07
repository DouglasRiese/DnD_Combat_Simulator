from classes import Zealot, Berserker

#Player stats
PROFICIENCY_BONUS = 3
# Simulation stats
SIMULATION_ROUNDS = 50000
ZEALOT_WIN_TOTAL = 0
BERSERKER_WIN_TOTAL = 0

count = 0
while count < SIMULATION_ROUNDS:
    MyZealot = Zealot(10, 100, 4)
    MyBerserker = Berserker(10, 100, 4)
    while MyZealot.HP > 0 and MyBerserker.HP > 0:
        MyZealot.HP -= MyBerserker.Attack()
        if MyBerserker.HP > 0:
            MyBerserker.HP -= MyZealot.Attack()
    if MyZealot.HP > 0:
        ZEALOT_WIN_TOTAL += 1
    else:
        BERSERKER_WIN_TOTAL += 1
    count += 1

print(f"Total wins zealot: {ZEALOT_WIN_TOTAL} Total wins berserker: {BERSERKER_WIN_TOTAL}")
# print(f"Average damage per round GWM: {TOTAL_DAMAGE_DEALT / SIMULATION_ROUNDS}")
#
# TOTAL_DAMAGE_DEALT = 0
# count = 0
# while count < SIMULATION_ROUNDS:
#     Attack(GWM_DAMAGE_BONUS = 0, MINIMUM_DAMAGE = 3)
#     count += 1
# print(f"Average damage per round GWF: {TOTAL_DAMAGE_DEALT / SIMULATION_ROUNDS}")