import weakref

from . import sudoku_utils
from .sudoku_utils import (
    square_indices,
    block_indices,
    SQUARE_COUNT,
)


class Cell(object):
    """Each cell holds a value and a set of possible values."""
    def __init__(self, val=None):
        self.val = val
        self.possible_vals = list(range(1, 10))
        self.ref_count = 0

    def __repr__(self):
        return 'Cell(val=%d, possible_vals=%r, ref_count=%d)' % (
            self.val, self.possible_vals, self.ref_count)


class Sudoku(object):
    """The Sudoku object holds the board, a list of cells, and a list of
    groups."""

    def __init__(self, board_string):
        self.cells = [Cell(int(val)) for val in board_string]
