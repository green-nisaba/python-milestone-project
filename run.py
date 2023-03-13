import random
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
winner = None
game_going = True


# Creating a board
def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])

# Receive user's input
def players_choice(board):
    choosen = int(input("Choose a number 1-9: "))
    if choosen >= 1 and choosen <= 9 and board[choosen - 1] == "-":
        board[choosen - 1] = current_player
    else:
        choosen = input("Invalid input. Choose a number 1-9, which was't taken:")



# Check for winner
def horizontal_winner(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[0]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def row_winner(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif  board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif  board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def diagonal_winner(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def whether_tie(board):
    global game_going
    if "-" not in board:
        display_board(board)
        print("It's a tie")
        game_going = False

def determine_winner(board):
    global game_going
    if horizontal_winner(board):
        display_board(board)
        print(f"The winner is {winner}!")
        game_going= False


    if row_winner(board):
        display_board(board)
        print(f"The winner is {winner}!")
        game_going= False

    if diagonal_winner(board):
        display_board(board)
        print(f"The winner is {winner}!")
        game_going= False
   

    
    
      
        

# Change player 
def change_player(): 
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


# Set computer move 
def comp_choice(board):
    while current_player == "O":
        comp_position = random.randint(0, 8)
        if board[comp_position] == "-":
            board[comp_position] = "O"
            change_player()

while game_going:
    display_board(board)
    players_choice(board)
    determine_winner(board)
    whether_tie(board)
    change_player()
    comp_choice(board)
    determine_winner(board)
    whether_tie(board)
   