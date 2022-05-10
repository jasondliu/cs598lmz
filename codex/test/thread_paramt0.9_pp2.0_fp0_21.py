import sys, threading
threading.Thread(target=lambda: sys.stdin.read(),daemon=True).start()

import copy
import pygame
from board import GameBoard
from solver import traverse

'''
Game board:
0 -> a cell that represents a free cell on the board.
1 -> a cell that represents a wall and thus not able to be moved to.
2 -> a cell that is part of the snake and thus should be painted a different color than the rest of the board on the screen.
3 -> a cell that represents food.
'''

