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
    if choosen >= 1 and choosen <=9 and board[choosen - 1] == "-":
        board[choosen - 1] = current_player
    else:
        print("Please choose a valid option")
