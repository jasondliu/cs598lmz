import threading
threading.stack_size(67108864)

from copy import deepcopy
from random import randint
from math import log2
import time
import sys

sys.setrecursionlimit(1000000)

class Node:
    def __init__(self, data, heuristic, depth, parent=None):
        self.data = data
        self.heuristic = heuristic
        self.depth = depth
        self.parent = parent

        self.val = self.heuristic + self.depth


class Puzzle:
    def __init__(self, table, heuristic):
        self.table = table
        self.heuristic = heuristic

    def get_neighbours(self):
        row, col = self.table.index(0)
        neighbours = []

        if row > 0:
            neighbour = deepcopy(self.table)
            neighbour[row][col], neighbour[row - 1][col] = neighbour[row - 1][col], neighbour[row][col]
            neighbours.append(Puzzle(neighbour, self.heuristic))

