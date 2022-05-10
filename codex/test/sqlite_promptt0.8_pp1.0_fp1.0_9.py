import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("test.db")
EAST = 0
SOUTH = 1
WEST = 2
NORTH = 3

class Wall:
    def __init__(self, is_wall, is_path, is_searched, is_blue_wall, is_yellow_wall, is_red_wall, is_green_wall, is_special_wall, is_other_wall):
        self.is_wall = is_wall
        self.is_path = is_path
        self.is_searched = is_searched
        self.is_blue_wall = is_blue_wall
        self.is_yellow_wall = is_yellow_wall
        self.is_red_wall = is_red_wall
        self.is_green_wall = is_green_wall
        self.is_special_wall = is_special_wall
        self.is_other_wall = is_other_wall


class Grid:
    def __init__(self, row, col):
        self.row = row
        self.col = col
