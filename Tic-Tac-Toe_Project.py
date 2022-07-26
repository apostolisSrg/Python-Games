board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]
         ]
# null board
print("   0    1    2")
print("  +---+---+---+")
print(str(0) + " | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
print("  +---+---+---+")
print(str(1) + " | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
print("  +---+---+---+")
print(str(2) + " | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
print("  +---+---+---+")
print("Tic_Tac_Toe Game")
print("")

# which player plays first
player = int(input("Type '1' or '2' for player1,player2 to start playing respectively: "))
print("")
while player < 1 or player > 2:
    print("Error")
    player = int(input("Type '1' or '2' for player1,player2 to start playing respectively: "))
    print("")
print("--player" + str(player) + " plays--")
print("")

# Choose a symbol
symbol = int(input("Type 0 for  symbol 'x' or 1 for symbol 'o': "))
while symbol < 0 or symbol > 1:
    print("Error")
    symbol = int(input("Type 0 for  symbol 'x' or 1 for symbol 'o': "))
print("")
if symbol == 0:
    print("--player" + str(player) + " chose the 'x' symbol--")
else:
    print("--player" + str(player) + " chose the 'o' symbol--")

# rounds
game_round = 0
active_game = True
while active_game:
    game_round += 1
    print("")

    # row choose
    a = int(input("Choose a row between 0 to 2: "))
    while a < 0 or a > 2:
        print("Error")
        a = int(input("Choose a row between 0 to 2: "))

    # column choose
    b = int(input("Choose a column between 0 to 2: "))
    while b < 0 or b > 2:
        print("Error")
        b = int(input("Choose a column between 0 to 2: "))
    print("")

    if board[a][b] == " " and symbol == 0:
        board[a][b] = "x"
        symbol = 1
    elif board[a][b] == " " and symbol == 1:
        board[a][b] = "o"
        symbol = 0
    else:
        print("The position you chose is already marked..Choose an empty box.")
        continue

    print("    0   1   2")
    print("  +---+---+---+")
    print(str(0) + " | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("  +---+---+---+")
    print(str(1) + " | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("  +---+---+---+")
    print(str(2) + " | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("  +---+---+---+")

    # check rows
    cnt_x = 0
    cnt_o = 0
    for j in range(0, len(board)):
        if board[0][j] == "x":
            cnt_x += 1
        if board[0][j] == "o":
            cnt_o += 1
    if cnt_x == len(board):
        print("")
        print("Tic Tac Toe. Player" + str(player) + " winner. Congratulations!")
        print("")
        break
    if cnt_o == len(board):
        print("")
        print("tic_tac_toe.Player" + str(player) + " winner. Congratulations!")
        print("")
        break

    cnt_x = 0
    cnt_o = 0
    for j in range(0, len(board)):
        if board[1][j] == "x":
            cnt_x += 1
        if board[1][j] == "o":
            cnt_o += 1
    if cnt_x == len(board):
        print("")
        print("Tic Tac Toe. Player" + str(player) + " winner. Congratulations!")
        print("")
        break
    if cnt_o == len(board):
        print("")
        print("tic_tac_toe.Player" + str(player) + " winner. Congratulations!")
        print("")
        break

    cnt_x = 0
    cnt_o = 0
    for j in range(0, len(board)):
        if board[2][j] == "x":
            cnt_x += 1
        if board[2][j] == "o":
            cnt_o += 1
    if cnt_x == len(board):
        print("")
        print("Tic Tac Toe. Player" + str(player) + " winner. Congratulations!")
        print("")
        break
    if cnt_o == len(board):
        print("")
        print("tic_tac_toe.Player" + str(player) + " winner. Congratulations!")
        print("")
        break

    # check columns
    cnt_x = 0
    cnt_o = 0
    for i in range(0, len(board)):
        if board[i][0] == "x":
            cnt_x += 1
        if board[i][0] == "o":
            cnt_o += 1
    if cnt_x == len(board):
        print("")
        print("Tic Tac Toe. Player" + str(player) + " winner. Congratulations!")
        print("")
        break
    if cnt_o == len(board):
        print("")
        print("tic_tac_toe.Player" + str(player) + " winner. Congratulations!")
        print("")
        break

    cnt_x = 0
    cnt_o = 0
    for i in range(0, len(board)):
        if board[i][1] == "x":
            cnt_x += 1
        if board[i][1] == "o":
            cnt_o += 1
    if cnt_x == len(board):
        print("")
        print("Tic Tac Toe. Player" + str(player) + " winner. Congratulations!")
        print("")
        break
    if cnt_o == len(board):
        print("")
        print("tic_tac_toe.Player" + str(player) + " winner. Congratulations!")
        print("")
        break

    cnt_x = 0
    cnt_o = 0
    for i in range(0, len(board)):
        if board[i][2] == "x":
            cnt_x += 1
        if board[i][2] == "o":
            cnt_o += 1
    if cnt_x == len(board):
        print("")
        print("Tic Tac Toe. Player" + str(player) + " winner. Congratulations!")
        print("")
        break
    if cnt_o == len(board):
        print("")
        print("tic_tac_toe.Player" + str(player) + " winner. Congratulations!")
        print("")
        break

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] == "x":
        print("tic_tac_toe.Player" + str(player) + " winner. Congratulations!")
        break
    if board[0][0] == board[1][1] == board[2][2] == "o":
        print("tic_tac_toe.Player" + str(player) + " winner. Congratulations!")
        break
    if board[0][2] == board[1][1] == board[2][0] == "x":
        print("tic_tac_toe.Player" + str(player) + " winner. Congratulations!")
        break
    if board[0][2] == board[1][1] == board[2][0] == "o":
        print("tic_tac_toe.Player" + str(player) + " winner. Congratulations!")
        break

    # Draw
    if game_round == 9:
        print("Draw!")
        break

    # next player
    if player == 1:
        print("--Turn of player2--")
        player = 2
        continue
    if player == 2:
        print("--Turn of player1--")
        player = 1
        continue

    # end of game
print("-------------------------")
print("|Game Over. Restart game|")
print("-------------------------")
