import ctypes
ctypes.CDLL('./lib/libomp.so.5', mode=ctypes.RTLD_GLOBAL)

# Load the C++ library
lib = ctypes.cdll.LoadLibrary('./lib/libsudoku.so')


# Function prototypes
lib.sudoku_solve.argtypes = [ctypes.c_char_p, ctypes.c_int]
lib.sudoku_solve.restype = ctypes.c_int

lib.sudoku_validate.argtypes = [ctypes.c_char_p, ctypes.c_int]
lib.sudoku_validate.restype = ctypes.c_int

lib.sudoku_generate.argtypes = [ctypes.c_char_p, ctypes.c_int]
lib.sudoku_generate.restype = ctypes.c_int


# Python versions of the functions
def solve(board):
    board = board.encode('utf-8')
    return lib.sudoku_solve(board,
