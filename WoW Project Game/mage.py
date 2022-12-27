from character import Character
from random import randrange


class Mage(Character):
    def __init__(self, name, equipment, attack_speed_indicator=2, delay_indicator=0):
        super().__init__(name, equipment, attack_speed_indicator, delay_indicator)
        self.attack_range = (8, 17)
        self.mana = 100
        self.max_mana = 100

    def end_round(self):
        super().end_round()
        if self.mana + 1 <= self.max_mana:
            self.mana += 1
        else:
            self.mana = self.max_mana

    def __lightning_spell(self):  # private method, only used from public method attack
        self.mana -= 55
        return randrange(30, 50)

    def attack(self):
        self.delay_indicator = self.max_delay_indicator - self.attack_speed_indicator
        if self.mana - 55 >= 0:
            return self.__lightning_spell()
        else:
            return round(randrange(self.attack_range[0], self.attack_range[1]) * self.equipment.sword)
