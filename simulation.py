from classes import Zealot, Berserker, Barbarian

class CombatSimulator:
    def __init__(self):
        #Player stats
        self.PROFICIENCY_BONUS = 3
        # Simulation stats
        self.SIMULATION_ROUNDS = 5000

    def attack(self, attacker, defender):
        defender.HP -= attacker.Melee_Attack()

    def round(self, first_combatant, second_combatant):

        while first_combatant.HP > 0 and second_combatant.HP > 0:
            self.attack(first_combatant, second_combatant)
            first_combatant.bonus_action()
            if second_combatant.HP > 0:
                self.attack(second_combatant, first_combatant)
                second_combatant.bonus_action()

        if first_combatant.HP > 0:
            first_combatant.WIN_TOTAL += 1
        else:
            second_combatant.WIN_TOTAL += 1

    def run_simulation(self):
        my_zealot = Zealot(10, 100, 4, 0)
        my_berserker = Berserker(10, 100, 4, 0)
        for _ in range(self.SIMULATION_ROUNDS):
            self.round(my_zealot, my_berserker)
            my_zealot.HP = 100
            my_berserker.HP = 100
            self.round(my_berserker, my_zealot)
            my_zealot.HP = 100
            my_berserker.HP = 100

        print(f"Total wins zealot: {my_zealot.WIN_TOTAL} Total wins berserker: {my_berserker.WIN_TOTAL}")


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