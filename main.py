board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

print("Let's play Tic Tac Toe!")

for line in board:
    for column in line:
        print(column, end=" ")
    print()

player = input("Choose your sign(X or O): ").upper()

while True:

    position = input(f"Player {player}, choose your position(line and column): ")
    line = int(position[0])
    column = int(position[1])

    while board[line][column] != "_":
        print("This position is already taken, choose another one")
        position = input(f"Player {player}, choose your position(line and column): ")
        line = int(position[0])
        column = int(position[1])

    board[line][column] = player

    for line in board:
        for column in line:
            print(column, end=" ")
        print()

    if player == "X":
        player = "O"
    else:
        player = "X"
