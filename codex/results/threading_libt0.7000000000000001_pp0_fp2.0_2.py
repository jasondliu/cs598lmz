import threading
threading.stack_size(2**27)
import sys
import imp

from board_util import GoBoardUtil
from gtp_connection import GtpConnection
from board_util import GoBoardUtil
from simple_board import SimpleGoBoard
from simple_board import SimpleGoBoardUtil
from pattern_util import PatternUtil

class Nogo():
    def __init__(self):
        """
        Player that selects moves randomly from the set of legal moves.
        Takes random simulations to atari.
        """
        self.name = "Nogo"
        self.version = 1.0
        self.debug_mode = False

    def get_move(self, board, color):
        board_copy = board.copy()
        max_num_simulations = 4
        move, num_simulations = self.uct(board_copy, max_num_simulations, color)
        return move

    def uct(self, board, num_simulations, color):
        if board.is_game_over():
            return None, None

        root = UCTNode(None, None
