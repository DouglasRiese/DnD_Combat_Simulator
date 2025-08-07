from classes import Zealot, Berserker, Barbarian

class CombatSimulator:
    def __init__(self):
        #Player stats
        self.PROFICIENCY_BONUS = 3
        # Simulation stats
        self.SIMULATION_ROUNDS = 10000
        self.ZEALOT_WIN_TOTAL = 0
        self.BERSERKER_WIN_TOTAL = 0

    def attack(self, attacker, defender):
        defender.HP -= attacker.Melee_Attack()

    def round(self):
        my_zealot = Zealot(10, 100, 4)
        my_berserker = Berserker(10, 100, 4)

        while my_zealot.HP > 0 and my_berserker.HP > 0:
            self.attack(my_zealot, my_berserker)
            if my_berserker.HP > 0:
                self.attack(my_berserker, my_zealot)

        if my_zealot.HP > 0:
            self.ZEALOT_WIN_TOTAL += 1
        else:
            self.BERSERKER_WIN_TOTAL += 1

    def run_simulation(self):
        for _ in range(self.SIMULATION_ROUNDS):
            self.round()

        print(f"Total wins zealot: {self.ZEALOT_WIN_TOTAL} Total wins berserker: {self.BERSERKER_WIN_TOTAL}")


simulator = CombatSimulator()
simulator.run_simulation()
# print(f"Average damage per round GWM: {TOTAL_DAMAGE_DEALT / SIMULATION_ROUNDS}")
#
# TOTAL_DAMAGE_DEALT = 0
# count = 0
# while count < SIMULATION_ROUNDS:
#     Attack(GWM_DAMAGE_BONUS = 0, MINIMUM_DAMAGE = 3)
#     count += 1
# print(f"Average damage per round GWF: {TOTAL_DAMAGE_DEALT / SIMULATION_ROUNDS}")