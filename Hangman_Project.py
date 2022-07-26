from random import randrange

words = ["clash", "response", "permanent", "solution", "divine", "consciousness", "stillness",
         "enlightenment", "accident", "congratulations", "rejection", "vitality", "mentality",
         "love", "robustness"]

hidden_word = words[randrange(0, len(words))]
active_game = True
guessed_letters = []
rounds = 0
while active_game:
    print(f"Round{rounds + 1}".rjust(10))
    while True:
        user_input = input("Give a letter: ").lower()
        user_input = user_input.strip()
        if not user_input.isalpha():
            print("You did not type a letter.Try again")
        elif len(user_input) != 1:
            print("Type only 1 character")
        else:
            break
    if user_input not in guessed_letters:
        guessed_letters.append(user_input)
        rounds += 1
    else:
        print("-You have already guessed this letter before-")
        continue

    print(f"The letter \"{user_input}\" occurs {hidden_word.count(user_input)} times in the hidden word")

    for char in hidden_word:
        if char in guessed_letters:
            print(char, end="")
        else:
            print("_", end="")

    print("\n")
    cnt = 0
    for i in hidden_word:
        if i in guessed_letters:
            cnt += 1
    if cnt == len(hidden_word):
        print(f"+{41 * '-'}+")
        print('You found the hidden word.Congratulations!!')
        print(f"+{41 * '-'}+")
        break
    if rounds == 15:
        print("You have reached the max attempts and you did not find the hidden word"
              ".Try again from start..")
        break
