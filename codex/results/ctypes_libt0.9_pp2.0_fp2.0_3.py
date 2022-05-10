import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Checkers")

# Setting initial game variables
computer_color = None
human_color = None
computer_pieces, human_pieces = None, None  # Sets of positions for all pieces
computer_men, human_men = None, None  # Sets of positions for men
computer_kings, human_kings = None, None  # Sets of positions for kings
computer_queens, human_queens = None, None  # Sets of positions for queen
selected_men, selected_kings, selected_queens = None, None, None

# Constants that have to do with the layout of the board, not game play

pieces = {  # Dictionary containing valid piece charaters
    "Black Men": "B", "Black Kings": "X", "Black Queens": "Q", "White Men": "W", "White Kings": "O", "White Queens": "U"
}

pieces_list = ["B", "X", "Q", "W", "O", "U"]  # List of all valid piece characters

board = []  # 2D List for
