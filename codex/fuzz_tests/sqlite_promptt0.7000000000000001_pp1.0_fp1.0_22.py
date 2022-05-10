import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# c.execute('CREATE TABLE points(x int, y int)')

class Point(Structure):
    _fields_ = [('x', c_int), ('y', c_int)]

class Rect(Structure):
    _fields_ = [('ul', Point), ('lr', Point)]

# Test sqlite3.connect
conn = sqlite3.connect('test.db')
c = conn.cursor()
#c.execute('CREATE TABLE points(x int, y int)')

# Test sqlite3.connect
sqlite3.connect('test.db')

# Test sqlite3.connect
sqlite3.connect('test.db')


class Game(object):
    """Game class"""
    def __init__(self, board, players, current_player, moves_taken):
        self.board = board
        self.players = players
        self.current_player = current_player
        self.moves_taken = moves_
