from equipment import Equipment
from random import randrange


class Character:
    def __init__(self, name, equipment, attack_speed_indicator=2, delay_indicator=0):
        self.name = name
        self.equipment = equipment
        self.health_indicator = 100 * self.equipment.cape
        self.max_health = 100 * self.equipment.cape
        self.attack_speed_indicator = attack_speed_indicator
        self.delay_indicator = delay_indicator
        self.max_delay_indicator = 5
        self.attack_range = (3, 11)

    def attack(self):
        self.delay_indicator = self.max_delay_indicator - self.attack_speed_indicator
        return round(randrange(self.attack_range[0], self.attack_range[1]) * self.equipment.sword)

    def is_dead(self):
        return self.health_indicator <= 0

    def end_round(self):
        if self.health_indicator + 1 <= self.max_health:
            self.health_indicator += 1
        else:
            self.health_indicator = self.max_health
        self.delay_indicator -= 1

    def __str__(self):
        st = "+------------------------------+" + "\n"
        st += f"| {('CHARACTER: ' + str(self.name)).center(29)}|" + "\n"
        st += f"| {''.center(29)}|" + "\n"
        st += f"| {('CURRENT HEALTH: ' + str(round(self.health_indicator))).center(29)}|" + "\n"
        st += f"| {('MAX HEALTH: ' + str(round(self.max_health))).center(29)}|" + "\n"
        st += f"| {('ATTACK SPEED: ' + str(self.attack_speed_indicator)).center(29)}|" + "\n"
        st += f"| {('DELAY: ' + str(self.delay_indicator)).center(29)}|" + "\n"
        st += "+------------------------------+"
        return st

    def __repr__(self):
        return f"Character({self.name},{self.attack_speed_indicator},{self.delay_indicator},{round(self.max_health)}," \
               f"{round(self.health_indicator)}) "

    def __iadd__(self, other):
        self.health_indicator += other
        return self

    def __isub__(self, other):
        self.health_indicator -= other
        return self


class Mage(Character):
    def __init__(self, name, equipment, attack_speed_indicator=2, delay_indicator=0):
        super().__init__()
