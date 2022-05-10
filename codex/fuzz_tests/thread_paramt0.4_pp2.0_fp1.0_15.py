import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

def print_board(board):
    for row in board:
        print(' '.join(row))

def create_board(size):
    board = []
    for i in range(size):
        board.append(['_'] * size)
    return board

def get_location():
    return (random.randint(0, len(board) - 1), random.randint(0, len(board) - 1))

def check_hit(guess, ship_loc):
    if guess == ship_loc:
        return True
    else:
        return False

def check_valid(guess):
    if guess[0] < 0 or guess[0] > len(board) - 1:
        return False
    if guess[1] < 0 or guess[1] > len(board) - 1:
        return False
    return True

def get_guess():
    guess = input('Guess the location of the ship (row, col): '
