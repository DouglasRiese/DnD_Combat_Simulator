from random import Random

class Barbarian:
    def __init__(self, AC:int, HP:int, level:int, WIN_TOTAL=0):
        self.AC = AC
        self.HP = HP
        self.level = level
        if self.level < 9:
            self.RAGE_DAMAGE_BONUS = 2
        elif self.level < 16:
            self.RAGE_DAMAGE_BONUS = 3
        else:
            self.RAGE_DAMAGE_BONUS = 4
        self.WIN_TOTAL = WIN_TOTAL

    def Reckless_Attack(self) -> int:
        first_to_hit_roll = Random().randint(1, 20)
        second_to_hit_roll = Random().randint(1, 20)

        return first_to_hit_roll if first_to_hit_roll > second_to_hit_roll else second_to_hit_roll

    def Attack_Damage(self, Min_DMG) -> int:
        first_damage_roll = Random().randint(Min_DMG, 6)
        second_damage_roll = Random().randint(Min_DMG, 6)
        return first_damage_roll + second_damage_roll

    def Melee_Attack(self, GWM_DAMAGE_BONUS=0, MINIMUM_DAMAGE=1, enemy_AC=10) -> int:
        total_damage = 0

        first_attack_to_hit_roll = self.Reckless_Attack()
        second_attack_to_hit_roll = self.Reckless_Attack()

        if first_attack_to_hit_roll >= enemy_AC:
            total_damage += self.Attack_Damage(MINIMUM_DAMAGE) + GWM_DAMAGE_BONUS
        if second_attack_to_hit_roll >= enemy_AC:
            total_damage += self.Attack_Damage(MINIMUM_DAMAGE) + GWM_DAMAGE_BONUS

        return total_damage

    def bonus_action(self):
        pass

class Zealot(Barbarian):
    def __init__(self, AC, HP, level, WIN_TOTAL):
        super().__init__(AC, HP, level, WIN_TOTAL)
        if self.level < 6:
            self.healing_dice = 4
        elif self.level < 12:
            self.healing_dice = 5
        elif self.level < 17:
            self.healing_dice = 6
        else:
            self.healing_dice = 7

    def Melee_Attack(self, GWM_DAMAGE_BONUS=0, MINIMUM_DAMAGE=1, enemy_AC=10):
        damage = super().Melee_Attack(GWM_DAMAGE_BONUS=0, MINIMUM_DAMAGE=1, enemy_AC=10)

        if damage > 0:
            damage += Random().randint(MINIMUM_DAMAGE, 6) + self.level / 2

        return damage

    def bonus_action(self):
        if self.HP < 50:
            for i in range(self.healing_dice):
                self.HP += Random().randint(1, 12)

class Berserker(Barbarian):
    def __init__(self, AC, HP, level, WIN_TOTAL):
        super().__init__(AC, HP, level, WIN_TOTAL)

    def Melee_Attack(self, GWM_DAMAGE_BONUS=0, MINIMUM_DAMAGE=1, enemy_AC=10):
        damage = super().Melee_Attack(GWM_DAMAGE_BONUS=0, MINIMUM_DAMAGE=1, enemy_AC=10)

        if damage > 0:
            for i in range(self.RAGE_DAMAGE_BONUS):
                damage += Random().randint(MINIMUM_DAMAGE, 6)

        return damage
