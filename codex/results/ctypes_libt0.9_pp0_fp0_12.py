import ctypes
ctypes.windll.kernel32.SetConsoleTitleW('Sudoku Solver')

class Sudoku():
    def __init__(self, game):
        self.game = game

    def get_row(self):
        for row in range(len(self.game)):
            for col in range(len(self.game)):
                if self.game[row][col] == 0:
                    return (row, col)

    def possible(self, row, col, val,):
        for x in range(0, 9):
            if self.game[row][x] == val: #look if val isn't already in column
                return False
            if self.game[x][col] == val: #look if val isn't already in row
                return False
        box_x = row // 3
        box_y = col // 3
        for x in range(box_x * 3, box_x * 3 + 3):
            for y in range(box_y * 3, box_y * 3 + 3):
                if self.game[x][y] == val: #look
