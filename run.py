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
