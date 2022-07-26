from random import randrange

table = ["scissors", "rock", "paper"]
active_game = True
user_score = 0
pc_score = 0
round_game = 0
history = []

while active_game:
    # rounds and scores
    if round_game >= 1:
        print(f"user score = {user_score}  ,  pc_score = {pc_score}")
        print("-----------------------------")
        history.append(f"Round{round_game}: user score = {user_score} , pc score = {pc_score}")
    print(f"Round{round_game + 1}:")
    # add score and info in history list for every round
    round_game += 1
    # check score and if game ends
    if user_score == 3:
        print("user wins game!! Congratulations")
        print("")
        print("History of game:")
        for i in history:
            print(i)
        break
    if pc_score == 3:
        print("pc wins game!! Congratulations")
        print("")
        print("History of game:")
        for i in history:
            print(i)
        break

    # user
    user_input = int(input("Choose 0 for 'scissors', 1 for 'rock', 2 for 'paper': "))
    while user_input < 0 or user_input > 2:
        print("type again...")
        user_input = int(input("Choose 0 for 'scissors', 1 for 'rock', 2 for 'paper': "))
    user = table[user_input]
    print(f"user chose '{user}'")

    # computer
    pc_input = randrange(0, len(table))
    pc = table[pc_input]
    print(f"pc chose '{pc}'")
    print("-----------------------------")

    # who wins the round
    if user == "rock":
        if pc == "scissors":
            print("           user wins")
            user_score += 1
            continue
        elif pc == "paper":
            print("           pc wins")
            pc_score += 1
            continue
        else:
            print("           draw")
            continue
    elif user == "scissors":
        if pc == "paper":
            print("           user wins")
            user_score += 1
            continue
        elif pc == "rock":
            print("           pc wins")
            pc_score += 1
            continue
        else:
            print("           draw")
            continue
    else:
        if pc == "rock":
            print("           user wins")
            user_score += 1
            continue
        elif pc == "scissors":
            print("           pc wins")
            pc_score += 1
            continue
        else:
            print("           draw")
            continue
