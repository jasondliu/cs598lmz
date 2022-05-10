import weakref

from . import utils
from . import enums
from . import game
from . import constants
from . import events
from . import properties
from . import actions


class Player(game.GameObject):
    """
    Represents the player in a game.

    This class is the main interface for interacting with the player.
    """

    def __init__(self, name="Player", **kwargs):
        """
        Initializes a new player.

        :param name: The name of the player.
        :type name: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.hand = properties.Hand()
        self.permanent_modifiers = properties.Modifiers()
        self.temporary_modifiers = properties.Modifiers()
        self.health = properties.Health()
        self.mana = properties.Mana()
        self.deck = properties.Deck()
        self.discard_pile = properties.DiscardPile()
        self.exhaust_pile = properties.ExhaustPile()

