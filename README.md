# Tic-tac-toe Game
Tic-tac-toe is originally a  paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O. 
The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. 
It is a solved game, with a forced draw assuming best play from both players.
More can be read on [Wikipedia page](https://en.wikipedia.org/wiki/Tic-tac-toe)


## How to play 
In this app user is playing against the computer. User is asked to choose a number from 1 to 9. 
Each number represents a spot on a gameboard. 
When there aren't empty spaces left, the game is over.

## Features 
### Existing features 
This app has:
* A simple board 
* Option to choose position on board

![screen](https://raw.githubusercontent.com/green-nisaba/python-milestone-project/main/screens/1_screen_ttt.png)


* Shows result of the game 

![result](https://raw.githubusercontent.com/green-nisaba/python-milestone-project/main/screens/2_screen_ttt.png)



### Future features 
* Add graphical interface
* Show user score counter 



## Data Model
I used Tic-tac-toe as a model. Game has several functions, that aim to print a board, to collect user input, to assign computer's input using random, and
to check for the winner. 

## Testing 
### Bugs
 * Some of functions didn't work as expected because of identation errors 
 * Game didn'g stop after victory as a result of incorrect function execution 

### Manual testing 
I tested my app doing the following:
* Cheching different outcomes of the game 
* Providing incorrect inpit (already taken spots on a board)
* Tested in my local and Heroku terminals

### Validator Testing 
PEP8 didn't find any significant issues(one line is too long)



## Deployment 

The project was deployed using terminal for Heroku.
Steps for deployment:
* Fork or clone this repository
* Create a new Heroku app
* Set the buildbacks to Python and NodeJS in this order
* Link the Heroku app to this repository
* Click on Deploy

## Credits 

* Code Institute for the deployment Terminal and [README example](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/)
* Wikipedia for details on "Tic-Tac-Toe" game
* [Clever Programmer](https://www.youtube.com/watch?v=n2o8ckO-lfk) for providing main approach on how to build the app 

