from character import Character


class Tank(Character):
    def __init__(self, name, equipment, attack_speed_indicator=2, delay_indicator=0):
        super().__init__(name, equipment, attack_speed_indicator, delay_indicator)
        self.attack_range = (20, 30)
        self.max_health *= 2
        self.health_indicator = self.max_health
