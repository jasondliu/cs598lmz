import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

from IPython.display import clear_output
from time import sleep
from random import randint
from IPython.display import clear_output

class Game():
    
    def __init__(self):
        self.board = [[' ']*3 for i in range(3)]
        self.turn = 'X'
        self.winner = None
        self.draw = False
        self.game_over = False
        
    def __repr__(self):
        return '\n'.join([' '.join(self.board[i]) for i in range(3)])
    
    def play(self):
        while not self.game_over:
            self.print_board()
            self.move()
            self.check_game()
            self.change_turn()
        self.print_board()
        if self.winner:
            print(f'{self.winner} won!')
