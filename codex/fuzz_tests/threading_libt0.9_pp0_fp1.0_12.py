import threading
threading.stack_size(2**27)
import sys

sys.path.append("../")
from prj4 import final_strategy
import project4_starter as strategy

class Game1(object):
    def __init__(self, players):
        """Initialize Game1 with the given players.

        Each player must have a 0, 1, or 2.
        raises ValueError if a player's number is outside 0-2
        """
        for player in players:
            if player not in (0, 1, 2):
                raise ValueError("Player not in (0, 1, 2)!")

        self.players = players
        self.state = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, \
                      1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

    def run(self):
        """Execute the actual game.

        Returns three values:
        1. winner -- the winner of the game (0, 1, or 2)
        2. history -- the history of the game
        3. cache
