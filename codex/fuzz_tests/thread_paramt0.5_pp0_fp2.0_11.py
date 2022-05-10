import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

def create_board():
    board = np.zeros((3, 3))
    return board

def place(board, player, position):
    if board[position] == 0:
        board[position] = player
    return board

def possibilities(board):
    return list(zip(*np.where(board == 0)))

def random_place(board, player):
    selection = possibilities(board)
    if len(selection) > 0:
        selection = np.random.choice(range(len(possibilities(board))), 1)[0]
        board[possibilities(board)[selection]] = player
    return board

def row_win(board, player):
    for i in range(len(board)):
        if np.all(board[i, :] == player):
            return True
    return False

def col_win(board, player):
    for i in range(len(board)):
        if np.all(board[:,
