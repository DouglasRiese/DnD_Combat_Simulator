from classes import Player

class CombatSimulator:
    def __init__(self):
        # Simulation stats
        self.SIMULATION_ROUNDS = 5000

    def attack(self, attacker, defender):
        defender.HP -= attacker.Melee_Attack()

    def combat(self, first_combatant, second_combatant):

        while first_combatant.HP > 0 and second_combatant.HP > 0:
            self.attack(first_combatant, second_combatant)
            first_combatant.bonus_action()
            if second_combatant.HP > 0:
                self.attack(second_combatant, first_combatant)
                second_combatant.bonus_action()

        if first_combatant.HP > 0:
            first_combatant.total_wins += 1
        else:
            second_combatant.total_wins += 1

    def run_simulation(self):

        first_player = Player(20, 14, 20, 10, 10, 10).Barbarian.Zealot
        second_player = Player(20, 14, 20, 10, 10, 10).Barbarian.Berserker
        for _ in range(self.SIMULATION_ROUNDS):
            self.combat(first_player, second_player)
            first_player.HP = 100
            second_player.HP = 100
            self.combat(second_player, first_player)
            first_player.HP = 100
            second_player.HP = 100

        print(f"Total wins zealot: {first_player.total_wins} Total wins berserker: {second_player.total_wins}")

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