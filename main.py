from random import choice
from time import sleep
import os


# use this function after move to clear console screen for better clarity
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# create board(row length = column length)
def initialize_board():
    return [["_" for _ in range(row_length)] for _ in range(column_length)]


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


def choose_game_mode():
    while True:
        mode = input("Choose the game mode (1 for Player vs. Player, 2 for Player vs. Computer): ")
        if mode == "1":
            print("You have chosen Player vs. Player mode.")
            return "PvP"
        elif mode == "2":
            print("You have chosen Player vs. Computer mode.")
            return "PvC"
        else:
            print("Invalid choice. Please enter 1 or 2.")


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


def check_possible_positions():
    possible_positions = []
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == "_":
                possible_positions.append((row, column))
    return possible_positions


def computer_move():
    if len(check_possible_positions()) > 0:
        computer_position = choice(check_possible_positions())
        row, column = int(computer_position[0]), int(computer_position[1])
        board[row][column] = computer_player
        return computer_player
    else:
        return None


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
                return False  # empty cell was found
    return True


while True:
    # initialization of the board
    row_length = 3
    column_length = row_length
    winning_streak_length = 3
    board = initialize_board()

    # the game
    print("Let's play Tic Tac Toe!\n")
    print_board()
    game_mode = choose_game_mode()
    current_player = get_player_sign()
    computer_player = switch_player(current_player)

    while True:
        clear_screen()
        print_board()

        if game_mode == "PvP":
            make_move()
            print_board()
            # check winner after every move
            winner = check_winner()
            if winner:
                clear_screen()
                print_board()
                print(f"Player {winner} wins!")
                break
            draw = check_draw()
            if draw is not False:
                clear_screen()
                print_board()
                print("It's a draw!")
                break
            current_player = switch_player(current_player)

        elif game_mode == "PvC":
            make_move()
            print_board()

            winner = check_winner()
            if winner:
                clear_screen()
                print_board()
                print(f"Player {winner} wins!")
                break
            draw = check_draw()
            if draw is not False:
                clear_screen()
                print_board()
                print("It's a draw!")
                break
            clear_screen()
            print_board()

            print("Computer turn...")
            sleep(1.5)

            computer_move()
            winner = check_winner()
            if winner:
                clear_screen()
                print(f"Player {winner} wins!")
                break
            draw = check_draw()
            if draw is not False:
                clear_screen()
                print("It's a draw!")
                break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        clear_screen()
        continue
    else:
        print(":(")
        break
