from random import Random

from openpyxl.packaging.manifest import Override


class Barbarian:
    def __init__(self, AC:int, HP:int, level:int):
        self.AC = AC
        self.HP = HP
        self.level = level
        if self.level < 9:
            self.RAGE_DAMAGE_BONUS = 2
        elif self.level < 16:
            self.RAGE_DAMAGE_BONUS = 3
        else:
            self.RAGE_DAMAGE_BONUS = 4

    def Reckless_Attack(self) -> int:
        First_To_Hit_Roll = Random().randint(1, 20)
        Second_To_Hit_Roll = Random().randint(1, 20)

        return First_To_Hit_Roll if First_To_Hit_Roll > Second_To_Hit_Roll else Second_To_Hit_Roll

    def Attack_Damage(self, Min_DMG) -> int:
        First_Damage_Roll = Random().randint(Min_DMG, 6)
        Second_Damage_Roll = Random().randint(Min_DMG, 6)
        return First_Damage_Roll + Second_Damage_Roll

    def Melee_Attack(self, GWM_DAMAGE_BONUS=3, MINIMUM_DAMAGE=1, enemy_AC=10) -> int:
        TOTAL_DAMAGE = 0

        First_Attack_To_Hit_Roll = self.Reckless_Attack()
        Second_Attack_To_Hit_Roll = self.Reckless_Attack()

        TOTAL_DAMAGE_BEFORE_ATTACKING = TOTAL_DAMAGE

        if First_Attack_To_Hit_Roll >= enemy_AC:
            TOTAL_DAMAGE += self.Attack_Damage(MINIMUM_DAMAGE) + GWM_DAMAGE_BONUS
        if Second_Attack_To_Hit_Roll >= enemy_AC:
            TOTAL_DAMAGE += self.Attack_Damage(MINIMUM_DAMAGE) + GWM_DAMAGE_BONUS

        # if TOTAL_DAMAGE > TOTAL_DAMAGE_BEFORE_ATTACKING:
        #     TOTAL_DAMAGE += Frenzy_Bonus_Damage(MINIMUM_DAMAGE)

        return TOTAL_DAMAGE

class Zealot(Barbarian):
    def __init__(self, AC, HP, level):
        super().__init__(AC, HP, level)

class Berserker(Barbarian):
    def __init__(self, AC, HP, level):
        super().__init__(AC, HP, level)

    def Melee_Attack(self, GWM_DAMAGE_BONUS=3, MINIMUM_DAMAGE=1, enemy_AC=10):
        Attack_Damage = super().Melee_Attack(GWM_DAMAGE_BONUS=3, MINIMUM_DAMAGE=1, enemy_AC=10)

        if Attack_Damage > 0:
            for i in range(self.RAGE_DAMAGE_BONUS):
                Attack_Damage += Random().randint(MINIMUM_DAMAGE, 6)

        return Attack_Damage
