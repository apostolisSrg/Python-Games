from equipment import Equipment
from character import Character
from mage import Mage
from tank import Tank
from arena import Arena
from random import uniform, randrange


def main():
    orcs = [Character(f'"Orc-{str(i + 1)}"', Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 2,
                      randrange(4)) for i in range(5)]
    night_elves = [Character(f'"Night-Elf-{str(i + 1)}"', Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 3,
                             randrange(3)) for i in range(3)]
    orcs.append(Tank(f'"Tank-Orc-{str(len(orcs) + 1)}"', Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 2, randrange(4)))
    night_elves.append(Mage(f'"Mage-Night-Elf-{str(len(night_elves) + 1)}"', Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)),
                            3, randrange(3)))
    a = Arena(orcs, night_elves)
    a.play()


try:
    main()
except KeyboardInterrupt as f:
    print("\n\n~The Battle interrupted from the Player~")
