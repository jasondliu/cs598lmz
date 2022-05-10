import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

from IPython.display import clear_output
from time import sleep
from random import randint

class Game():
    def __init__(self, rows=3, cols=3, win_length=3, player_one="Player 1", player_two="Player 2"):
        self.rows = rows
        self.cols = cols
        self.win_length = win_length
        self.player_one = player_one
        self.player_two = player_two
        self.board = [[' '] * self.cols for _ in range(self.rows)]
        self.turn = 1
        self.winner = None
        self.winners_move = None
    
    def is_empty(self, row, col):
        return self.board[row][col] == ' '
    
    def get_player(self):
        return self.player_one if self.turn == 1 else self.player_two
    
    def place_piece
