from random import Random
from enum import Enum

class SubClass(Enum):
    BERSERKER = "Berserker"
    ZEALOT = "Zealot"

class Player:
    def __init__(self, str, dex, con, int, wis, cha):
        (self.str, self.dex, self.con, self.int, self.wis, self.cha) = str, dex, con, int, wis, cha
        self.total_wins = 0
        self.bonus_dmg = 0
        self.Feats = self.Feats(self)
        self.barbarian = self.Barbarian(self)
        self.fighter = self.Fighter(self)
        self.character_level = 0
        #TODO: these ifs need to not just run on init
        if self.character_level < 5:
            self.proficiency = 2
        elif self.character_level < 9:
            self.proficiency = 3
        elif self.character_level < 13:
            self.proficiency = 4
        elif self.character_level < 17:
            self.proficiency = 5
        else:
            self.proficiency = 6

    class Feats:
        def __init__(self, player):
            self.player = player

        def Great_Weapon_Master(self):
            self.player.bonus_dmg += self.player.proficiency

    class Barbarian:
        def __init__(self, player, AC:int, HP:int, level:int, subclass = None):
            (self.player, self.AC, self.HP, self.level) = player, AC, HP, level
            self.subclass = subclass

            self.player.character_level += level
            if self.level < 9:
                self.rage_damage_bonus = 2
            elif self.level < 16:
                self.rage_damage_bonus = 3
            else:
                self.rage_damage_bonus = 4

            if self.subclass.ZEALOT:
                self.subclass = self.Zealot(self)
            if self.subclass.BERSERKER:
                self.subclass = self.Berserker(self)

        def Reckless_Attack(self) -> int:
            first_to_hit_roll = Random().randint(1, 20)
            second_to_hit_roll = Random().randint(1, 20)

            return first_to_hit_roll if first_to_hit_roll > second_to_hit_roll else second_to_hit_roll

        def Attack_Damage(self, min_dmg) -> int:
            first_damage_roll = Random().randint(min_dmg, 6)
            second_damage_roll = Random().randint(min_dmg, 6)
            return first_damage_roll + second_damage_roll

        def Melee_Attack(self, GWM_bonus_dmg=0, min_dmg=1, enemy_AC=10) -> int:
            total_damage = 0

            first_attack_to_hit_roll = self.Reckless_Attack()
            second_attack_to_hit_roll = self.Reckless_Attack()

            if first_attack_to_hit_roll >= enemy_AC:
                total_damage += self.Attack_Damage(min_dmg) + GWM_bonus_dmg
            if second_attack_to_hit_roll >= enemy_AC:
                total_damage += self.Attack_Damage(min_dmg) + GWM_bonus_dmg

            return total_damage

        def bonus_action(self):
            pass

        class Zealot:
            def __init__(self, barbarian):
                super().__init__()
                self.barbarian = barbarian
                if self.barbarian.level < 6:
                    self.healing_dice = 4
                elif self.barbarian.level < 12:
                    self.healing_dice = 5
                elif self.barbarian.level < 17:
                    self.healing_dice = 6
                else:
                    self.healing_dice = 7

            def Melee_Attack(self, GWM_bonus_dmg=0, min_dmg=1, enemy_AC=10):
                damage = self.barbarian.Melee_Attack(GWM_bonus_dmg=0, min_dmg=1, enemy_AC=10)

                if damage > 0:
                    damage += Random().randint(min_dmg, 6) + self.barbarian.level / 2

                return damage

            def bonus_action(self):
                if self.barbarian.HP < 50:
                    for i in range(self.healing_dice):
                        self.barbarian.HP += Random().randint(1, 12)

        class Berserker:
            def __init__(self, barbarian):
                self.barbarian = barbarian
                super().__init__()

            def Melee_Attack(self, GWM_bonus_dmg=0, min_dmg=1, enemy_AC=10):
                damage = self.barbarian.Melee_Attack(GWM_bonus_dmg=0, min_dmg=1, enemy_AC=10)

                if damage > 0:
                    for i in range(self.barbarian.rage_damage_bonus):
                        damage += Random().randint(min_dmg, 6)

                return damage

    class Fighter:
        def __init__(self, player, AC: int, HP: int, level: int, subclass=None):
            (self.player, self.AC, self.HP, self.level, self.total_wins) = player, AC, HP, level, 0
            self.subclass = subclass