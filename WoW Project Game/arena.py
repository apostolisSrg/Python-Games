from character import Character
from random import randrange


class Arena:
    def __init__(self, team_A, team_B):
        self.team_A = team_A
        self.team_B = team_B

    def __str__(self):
        st = f"{' ' * 11} TEAM A" + "\n"
        for characters in self.team_A:
            st += str(characters) + "\n"
        st += f"{' ' * 11} TEAM B" + "\n"
        for characters in self.team_B:
            st += str(characters) + "\n"
        return st

    def __repr__(self):
        st = f"Arena(["
        st += ", ".join([repr(character) for character in self.team_A])
        st += "],["
        st += ", ".join([repr(character) for character in self.team_B])
        st += "])"
        return st

    def play(self):
        time = -1
        while True:
            time += 1
            print("=============")
            print(f"TIME: {time}")
            print("=============")
            print(self)
            characters_ready_to_attack_team_A = [characters for characters in self.team_A if
                                                 characters.delay_indicator == 0]
            characters_ready_to_attack_team_B = [characters for characters in self.team_B if
                                                 characters.delay_indicator == 0]
            if time == 0:
                print("The Battle Arena is ready!")
                print("")
                input("Press Enter to start the Battle: ").strip()
                print("")
            if not characters_ready_to_attack_team_A and not characters_ready_to_attack_team_B:
                print("No attacks in this round!")
            else:
                if characters_ready_to_attack_team_A:
                    for character in characters_ready_to_attack_team_A:
                        attacker = character
                        enemy = self.team_B[randrange(len(self.team_B))]
                        damage = attacker.attack()
                        enemy.health_indicator -= damage
                        print(f"{character.name} -({damage} DMG)-> {enemy.name}")
                if characters_ready_to_attack_team_B:
                    for character in characters_ready_to_attack_team_B:
                        attacker = character
                        enemy = self.team_A[randrange(len(self.team_A))]
                        damage = attacker.attack()
                        enemy.health_indicator -= damage
                        print(f"{character.name} -({damage} DMG)-> {enemy.name}")
            print("\nDEATHS:")
            for pos in range(len(self.team_A) - 1, -1, -1):
                if self.team_A[pos].is_dead():
                    print(f"{self.team_A[pos].name}")
                    self.team_A.pop(pos)
            for pos in range(len(self.team_B) - 1, -1, -1):
                if self.team_B[pos].is_dead():
                    print(f"{self.team_B[pos].name}")
                    self.team_B.pop(pos)

            if len(self.team_A) == 0:
                print("")
                print("Team B won!")
                break
            elif len(self.team_B) == 0:
                print("")
                print("Team A won!")
                break

            for character in self.team_A:
                character.end_round()
            for character in self.team_B:
                character.end_round()
            print("")
            input("Press Enter to continue the Battle: ").strip()
