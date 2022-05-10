import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

def check_win(board, player):
    if board[0] == board[1] == board[2] == player: return True
    if board[3] == board[4] == board[5] == player: return True
    if board[6] == board[7] == board[8] == player: return True
    if board[0] == board[3] == board[6] == player: return True
    if board[1] == board[4] == board[7] == player: return True
    if board[2] == board[5] == board[8] == player: return True
    if board[0] == board[4] == board[8] == player: return True
    if board[2] == board[4] == board[6] == player: return True
    return False

def check_no_winner(board):
    if "-" not in board:
        return True
    return False

class Game:
    def __init__(self, p1, p2):
        self
