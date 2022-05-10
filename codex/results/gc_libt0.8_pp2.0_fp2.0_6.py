import gc, weakref
from typing import List
import pickle

from cube import Cube
from players import CubePlayer


class Agent:
    # ID attribution variables
    _agent_count = 1
    _agent_list = []

    def __init__(self, name: str, players: List[CubePlayer]):
        self.name = name
        self.players = players
        self.cube = Cube()
        self.id = Agent._agent_count
        Agent._agent_count += 1
        Agent._agent_list.append(weakref.proxy(self))

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f'Agent({self.name}, {self.cube}, {self.players})'

    def _init(self):
        self.cube.setup_cube()

    def update_cube(self, cube: Cube):
        self.cube = cube

    @
