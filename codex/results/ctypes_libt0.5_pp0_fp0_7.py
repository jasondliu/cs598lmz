import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Fantastic Four")

# -- Global variables --
# Game objects
board = [[" "," "," "],[" "," "," "],[" "," "," "]]

# Game variables
continue_game = True

# -- Functions --
#
# Function Name: display_board
# Purpose: to display the tic-tac-toe board
# Parameter: None
# Pre-condition: the board must be initialized
# Post-condition: the board is displayed
def display_board():
    print("   1   2   3")
    print("1  "+board[0][0]+" | "+board[0][1]+" | "+board[0][2])
    print("  ---|---|---")
    print("2  "+board[1][0]+" | "+board[1][1]+" | "+board[1][2])
    print("  ---|---|---")
    print("3  "+board[2][0]+" | "+board[2][1]+" | "+board[2][2])


