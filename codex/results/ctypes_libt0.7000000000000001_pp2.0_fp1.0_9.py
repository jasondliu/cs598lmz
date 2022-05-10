import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Python Tic Tac Toe")


class TicTacToe:

    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.player = 'X'
        self.player_dict = {
            'X': 'O',
            'O': 'X'
        }

    def print_board(self):
        print(' ' + self.board[0][0] + ' | ' + self.board[0][1] + ' | ' + self.board[0][2])
        print('---|---|---')
        print(' ' + self.board[1][0] + ' | ' + self.board[1][1] + ' | ' + self.board[1][2])
        print('---|---|---')
        print(' ' + self.board[2][0] + ' | ' + self.board[2][1] + ' | ' + self.board
