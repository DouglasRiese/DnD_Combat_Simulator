from random import Random

# Player stats
PROFICIENCY_BONUS = 3
# Enemy stats
ENEMY_ARMOR_CLASS = 11
# Simulation stats
SIMULATION_ROUNDS = 50000
ZEALOT_WIN_TOTAL = 0
BERSERKER_WIN_TOTAL = 0

class Barbarian:
    def __init__(self, HP:int, level:int):
        self.HP = HP
        self.level = level

    def Reckless_Attack(self) -> int:
        First_To_Hit_Roll = Random().randint(1, 20)
        Second_To_Hit_Roll = Random().randint(1, 20)

        return First_To_Hit_Roll if First_To_Hit_Roll > Second_To_Hit_Roll else Second_To_Hit_Roll

    def Attack_Damage(self, Min_DMG) -> int:
        First_Damage_Roll = Random().randint(Min_DMG, 6)
        Second_Damage_Roll = Random().randint(Min_DMG, 6)
        return First_Damage_Roll + Second_Damage_Roll

    def Attack(self, GWM_DAMAGE_BONUS=PROFICIENCY_BONUS, MINIMUM_DAMAGE=1) -> int:
        TOTAL_DAMAGE = 0

        First_Attack_To_Hit_Roll = self.Reckless_Attack()
        Second_Attack_To_Hit_Roll = self.Reckless_Attack()

        TOTAL_DAMAGE_BEFORE_ATTACKING = TOTAL_DAMAGE

        if First_Attack_To_Hit_Roll >= ENEMY_ARMOR_CLASS:
            TOTAL_DAMAGE += self.Attack_Damage(MINIMUM_DAMAGE) + GWM_DAMAGE_BONUS
        if Second_Attack_To_Hit_Roll >= ENEMY_ARMOR_CLASS:
            TOTAL_DAMAGE += self.Attack_Damage(MINIMUM_DAMAGE) + GWM_DAMAGE_BONUS

        # if TOTAL_DAMAGE > TOTAL_DAMAGE_BEFORE_ATTACKING:
        #     TOTAL_DAMAGE += Frenzy_Bonus_Damage(MINIMUM_DAMAGE)

        return TOTAL_DAMAGE

class Zealot(Barbarian):
    def __init__(self, HP, level):
        super().__init__(HP, level)

class Berserker(Barbarian):
    def __init__(self, HP, level):
        super().__init__(HP, level)

    def Frenzy_Bonus_Damage(Min_DMG):
        First_Damage_Roll = Random().randint(Min_DMG, 6)
        Second_Damage_Roll = Random().randint(Min_DMG, 6)

        return First_Damage_Roll + Second_Damage_Roll

MyZealot = Zealot(100, 4)
MyBerserker = Berserker(100, 4)

count = 0
while count < SIMULATION_ROUNDS:
    while MyZealot.HP > 0 and MyBerserker.HP > 0:
        MyBerserker.HP -= MyZealot.Attack()
        if MyBerserker.HP > 0:
            MyZealot.HP -= MyBerserker.Attack()
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
