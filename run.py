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


def prepare_computer_ship():
    for x in range(total_ship_number):
        computer_ship_row.append(random_num(computer_board))
        computer_ship_col.append(random_num(computer_board))


def take_input_and_play_game():
    global user_guess_row, user_guess_col, computer_guess_row
    global computer_guess_col

    while True:
        """
        Validation! user can guess row from index nummer o and it's depend
        on users grid size otherwise print wrong message below.
        """
        try:
            user_guess_row = int(input("Guess a row:\n "))
            if user_guess_row < 0 or user_guess_row >= user_grid_size:
                print("Oops, that's not even in the ocean. Guess again:\n")
                continue
        except ValueError:
            print("Please enter correct row value:\n")
            continue
        else:
            break
    
    while True:
        """
        Validation! user can guess colum from index nummer o and it's depend
        on users grid size otherwise print wrong message below.
        """
        try:
            user_guess_col = int(input("Guess a col:\n"))
            if user_guess_col < 0 or user_guess_col >= user_grid_size:
                print("Oops, that's not even in the ocean. Guess again:\n")
                continue
        except ValueError:
            print("Please enter correct col value:\n")
            continue
        else:
            break
    
    computer_guess_row = random_num(computer_board)
    computer_guess_col = random_num(computer_board)
    show_result()


def show_result():
    """
    In the result board if player guess Correct then print Congratulations
    eser_name win, otherwise missed this time. Computer board print also
    like same to user board.
    """
    if computer_guess_row == user_ship_row[0] and\
            computer_guess_col == user_ship_col[0]:
        user_board[computer_guess_row][computer_guess_col] = hit_success_sign
        print_board(user_board, user_name)
        print("\n")
        print("Computer guess to user board...")
        sleep(2)
        print("Congratulations! computer guess this time.")
    else:
        user_board[computer_guess_row][computer_guess_col] = hit_miss_sign
        print_board(user_board, user_name)
        print("\n")
        print("Computer guess to user board...")
        sleep(2)
        print("Computer missed this time.")
    
    if user_guess_row == computer_ship_row[0] and\
            user_guess_col == computer_ship_col[0]:
        computer_board[user_guess_row][user_guess_col] = hit_success_sign
        print_board(computer_board, computer_name)
        print("\n")
        print(user_name + " guess to computer board...")
        sleep(2)
        print("Congratulations! " + user_name + " guess this time")
    else:
        computer_board[user_guess_row][user_guess_col] = hit_miss_sign
        print_board(computer_board, computer_name)
        print("\n")
        print(user_name + " guess to computer board...")
        sleep(2)
        print(user_name + " missed this time.")