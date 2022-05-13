from random import randint
from time import sleep

"""
Import random go to generate random int in game.
Import sleep from time, is used to add delay in the exacution of a program
"""
print("---------------------------------- \n"
      "Wellcome to ULTIMATE BATTLESHIP! \n"
      "Board size player can decide. \n"
      "Top left corner is raw: 0, col: 0 \n"
      "Grid size between 5 to 10 \n"
      "---------------------------------- ")

user_board = []
computer_board = []
total_ship_number = 5
user_grid_size = -1
max_grid_size = 10
min_grid_size = 5
user_guess_row = -1
user_guess_col = -1
computer_guess_row = -1
computer_guess_col = -1
user_ship_row = []
user_ship_col = []
computer_ship_row = []
computer_ship_col = []
user_name = ""
computer_name = "Computer"
ship_sign = "  @  "
hit_success_sign = "  X  "
hit_miss_sign = "  0  "
game_rounds = 3


def set_user_up(user_name):
    while True:
        user_name = input("Please enter your name:\n ")
        user_name = user_name.strip()
        """
        User name validation! User name must be letters or numbers.
        """
        if len(user_name) > 0:
            break
        else:
            print("Invalid! Please enter valid user name")

    while True:
        """
        Grid size validation inside the try, user can choose minimum grid
        size 5 and maximum grid size 10 and except NameError and ValueError
        """
        try:
            user_grid_size = int(input("Please enter grid size num (5-10): "))
            if user_grid_size < min_grid_size or\
               user_grid_size > max_grid_size:
                print("Please enter valid grid size number between (5-10): ")
                continue
        except (NameError, SyntaxError, ValueError):
            print("Please enter valid grid size number:")
            continue
        else:
            break
    
    for x in range(user_grid_size):
        user_board.append(['  .  '] * user_grid_size)
    
    for x in range(user_grid_size):
        computer_board.append(['  .  '] * user_grid_size)


def print_board(board, name):
    """ Print User board and stands username on the board """
    print("\n")
    print(name + "'s board")
    print("------------------------------------------------------------")
    for row in board:
        print(" ".join(row))


def random_num(board):
    return randint(0, len(board) - 1)


def prepare_user_ship():
    for x in range(total_ship_number):
        user_ship_row.append(random_num(user_board))
        user_ship_col.append(random_num(user_board))
        user_board[user_ship_row[x]][user_ship_col[x]] = ship_sign