# ULTIMATE Battleships Game

Ultimate Battleships is a Python terminal game, which runs in the Code Institute mock terminal on Heroku

Users can try to guess in the computer board by finding all of the computer's ballteships before the computer finds theirs. Each battleship is @ sign on the board

- Here is the live version of my project
![live verson different screen](images/screenshot.png)


## How to play
Ultimate Battleships is based on the classic pen-and-paper game. You can read more about it on Wikipedia. 
In this version, user enters their name and two boards are rendomly printed.
The player can see where their ships are, shows by an @ sign, but user cannot see where the computer's ships are.
Guesses are marked on the board with an X. Hits are indicated by 0.
User and the computer then take it in turns to make guesses and try to sink each other's battleships.
The winner is who sinks of there battleships first.

## Features

#### Existing Features
    - Random board generation
        - Ships are rendomly placed on both the user and computer boards
        - The user cannot see where the computer's ships are
![screenship1.png](images/screenshot1.png)

* User can play against the computer
* Accept user input row and column

![screenshot2.png](images/screenshot2.png)

* Input validation and error checking
    - User cannot enter coordinate outside the size of the grid
    - User must enter numbers
![screenshot3.png](images/screenshot3.png)

#### Future Features
- Allow user to select the board size and number of ships 
- Allow user to position ships themeselves


## Testing

I have manually tested this project by doing the following
- Passed the code through a PEP linter and confirmed that there are no problems
- Given incorrect input: strings when numbers are expected, out of bounds inputs
- Tested in my local terminal and the code Institute Heroku Terminal


## Bugs

### Solved Bugs
    - When I wrote the project, I was getting problem guessing ships on computer board. I fixed this problem by adding two function, one is is_computer_guess_success() and another one is is_user_guess_success()
    - This function was guess ships sign properly on computer board and user board

## Remaining Bugs
    - No bugs remaining

## Validator Testing
    - PEP8
        * No errors were returned from PEP8online.com

## Deployment 
This project was deployed using Code Institute's mock terminal for Heroku.

    * Steps for deployment:
        - install heroku CLI on mac terminal
        - heroku login (gitpod)
        - heroku git:remote -a portfolio-p3-battleship-game
        - git add .
        - git commit -m "make it better"
        - git push heroku HEAD:master

## Deployment Link
    - Heroku deploy link: https://portfolio-p3-battleship-game.herokuapp.com/
    - Github link: https://github.com/mamuzaan/portfolio-p3-battleship-game

## Credits
- Code Institute for the deployment terminal
- Wikipedia for the details of the battleship game
- Game comcept from stack overflow.
- Mentor support

