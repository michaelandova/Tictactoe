def initialize_board(row_length, column_length):
    return [["_" for _ in range(row_length)] for _ in range(column_length)]


def is_position_out_of_range(row, column, board):
    return row < 0 or row >= len(board) or column < 0 or column >= len(
        board[0])


def print_board(board):
    # print the first row with column numbers
    col_numbers = "  ".join(f"{i:2}" for i in range(len(board[0])))
    print("    " + col_numbers)

    # print the rest of the table with row numbers at the beginning
    for i in range(len(board)):
        row = board[i]
        print(f"\n{i:2}  ", end=" ")
        for cell in row:
            print(f"{cell:2} ", end=" ")
        print()


def get_player_sign():
    while True:
        player = input("\nChoose your sign (X or O): ").upper()
        if player in ["X", "O"]:
            return player
        else:
            print("Invalid sign!\n")


def switch_player(player):
    return "O" if player == "X" else "X"


def make_move(player, board):
    while True:
        position = input(
            f"Player {player}, choose your position (row and column): ")

        if len(position) == 2 and position[0].isdigit(
        ) and position[1].isdigit():
            row, column = int(position[0]), int(position[1])

            if is_position_out_of_range(row, column, board):
                print("This position is out of range, choose another one")
            elif board[row][column] != "_":
                print("This position is already taken, choose another one")
            else:
                board[row][column] = player
                break
        else:
            print(
                "Invalid input, please enter two digits representing row and column."
            )


def check_next(row, column, d_row, d_column, board):
    player = board[row][column]
    for i in range(1, winning_streak_length):
        next_row = row + i * d_row
        next_column = column + i * d_column

        if (next_row < 0 or next_row >= len(board) or next_column < 0
                or next_column >= len(board[0])
                or board[next_row][next_column] != player):
            return False
    return True


def check_winner(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] != "_" and (
                    check_next(row, column, 1, 0, board)  # Check rows
                    or check_next(row, column, 0, 1, board)  # Check columns
                    or check_next(row, column, 1, 1, board)  # Check diagonal \
                    or check_next(row, column, 1, -1,
                                  board)  # Check diagonal /
            ):
                return board[row][column]  # winner found
    return None  # if no winner


def check_draw(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == "_" and check_winner(board) is None:
                return False  # empty cell and no winner was found


# initialization of the board
row_length = 5
column_length = row_length
winning_streak_length = 3
board = initialize_board(row_length, column_length)

# the game
print("Let's play Tic Tac Toe!\n")
print_board(board)
player = get_player_sign()

while True:
    make_move(player, board)
    print_board(board)

    #check winner after every move
    winner = check_winner(board)
    if winner:
        print(f"Player {winner} wins!")
        break
    draw = check_draw(board)
    if draw is not False:
        print("It's a draw!")
        break
    player = switch_player(player)
