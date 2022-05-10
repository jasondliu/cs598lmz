import gc, weakref
import numpy as np

from pybrain.rl.environments.task import Task
from pybrain.rl.environments.environment import Environment
from pybrain.rl.environments.episodic import EpisodicTask
from pybrain.rl.environments.twoplayergames.twoplayergame import TwoPlayerGame
from pybrain.rl.environments.twoplayergames.gamestate import GameState
from pybrain.rl.environments.twoplayergames.gametools import *


class TwoPlayerGameTask(EpisodicTask):
    """ A task for playing a two-player game, either against a player or
        against an agent.
    """

    def __init__(self, environment, game, player=1, opponent=None):
        """ Create a task for playing a two-player game.

            `environment`:  the environment in which the game is played.
            `game`:         a subclass of TwoPlayerGame that implements the
                            game rules.
            `player`:       the player number of the agent (1 or 2).
            `opponent`:     the opponent
