def initialize_board(num_rows, num_columns):
    return [["_" for _ in range(num_rows)] for _ in range(num_columns)]


def is_position_out_of_range(row, column):
    return row < 0 or row >= len(board) or column < 0 or column >= len(
        board[0])


def print_board():
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


def make_move():
    while True:
        position = input(
            f"Player {current_player}, choose your position (row and column): ")

        if len(position) == 2 and position[0].isdigit(
        ) and position[1].isdigit():
            row, column = int(position[0]), int(position[1])

            if is_position_out_of_range(row, column):
                print("This position is out of range, choose another one")
            elif board[row][column] != "_":
                print("This position is already taken, choose another one")
            else:
                board[row][column] = current_player
                break
        else:
            print(
                "Invalid input, please enter two digits representing row and column."
            )


def check_next(row, column, d_row, d_column):
    player = board[row][column]
    for i in range(1, winning_streak_length):
        next_row = row + i * d_row
        next_column = column + i * d_column

        if (next_row < 0 or next_row >= len(board) or next_column < 0
                or next_column >= len(board[0])
                or board[next_row][next_column] != player):
            return False
    return True


def check_winner():
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] != "_" and (
                    check_next(row, column, 1, 0)  # Check rows
                    or check_next(row, column, 0, 1)  # Check columns
                    or check_next(row, column, 1, 1)  # Check diagonal \
                    or check_next(row, column, 1, -1)  # Check diagonal /
            ):
                return board[row][column]  # winner found
    return None  # if no winner


def check_draw():
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == "_":
                return False  # empty cell and no winner was found
    return True


while True:
    # initialization of the board
    row_length = 3
    column_length = row_length
    winning_streak_length = 4
    board = initialize_board(row_length, column_length)

    # the game
    print("Let's play Tic Tac Toe!\n")
    print_board()
    current_player = get_player_sign()

    while True:
        make_move()
        print_board()

        # check winner after every move
        winner = check_winner()
        if winner:
            print(f"Player {winner} wins!")
            break
        draw = check_draw()
        if draw is not False:
            print("It's a draw!")
            break
        current_player = switch_player(current_player)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
