import gc, weakref
import math

"""
This is a simple implementation of the A* algorithm.
It's designed to be easily understandable, not fast.

The class AStarSolver provides the public method astar_search
which returns a list of actions going from the start state to the
goal state, or None if no solution was found.
"""

class AStarSolver:
    def __init__(self, map_, map_size):
        self.map = map_
        self.map_size = map_size
        self.actions = [(1,0), (0,1), (-1,0), (0,-1)]
        self.actions_name = ["RIGHT", "DOWN", "LEFT", "UP"]
        self.goal_state = None
        self.start_state = None
        self.open_list = []
        self.closed_list = []
        self.path = []
        self.nodes_expanded = 0
        self.max_depth_reached = 0
        self.running_time = 0
        self.max_search_depth = 0

