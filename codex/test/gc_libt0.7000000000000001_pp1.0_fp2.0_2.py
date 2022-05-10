import gc, weakref
from math import sqrt, log
from collections import deque

gc.collect()


class Node(object):
    """
    A node in the game tree. Note wins is always from the viewpoint of playerJustMoved.
    Crashes if state not specified.
    """

    def __init__(self, move=None, parent=None, state=None):
        self.move = move  # the move that got us to this node - "None" for the root node
        self.parentNode = parent  # "None" for the root node
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.untriedMoves = state.get_moves()  # future child nodes
        self.playerJustMoved = state.player_just_moved  # the only part of the state that the Node needs later

