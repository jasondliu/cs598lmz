import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Constants
ADDRESS = ''
PORT = 65432

# Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ADDRESS, PORT))
sock.listen()

# Set up game
board = []
turn = 'X'
winner = None

# Init board
for i in range(3):
    board.append([])
    for j in range(3):
        board[i].append(None)

# Print board
def print_board():
    print('---------')
    for i in range(3):
        print('|', end='')
        for j in range(3):
            if board[i][j] == None:
                print(' ', end='')
            else:
                print(board[i][j], end='')
            print('|', end='')
        print()
        print('---------')

# Check winner
