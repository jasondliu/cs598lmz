import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()
# This is a function that prints the board that it was passed. Returns None.
def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
# This is a function that takes in a board and a move and then places
# the move on the board.
def make_move(board, move, player):
    board[move] = player
# This is a function that takes in a board and a player and then checks to see if
# that player has won. Returns True if so, otherwise False.
def check_win(board, player):
   
