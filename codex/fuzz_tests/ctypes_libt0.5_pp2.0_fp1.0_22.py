import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("TicTacToe")

print("Welcome to Tic-Tac-Toe!")

#Create a list to store the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#If game is still going
game_still_going = True

#Who won or tie
winner = None

#Whos turn is it
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#Play a game of tic tac toe
def play_game():
    #Display the initial board
    display_board()

    #While the game is still going
    while game_still_going:
        #Handle a single turn of an
