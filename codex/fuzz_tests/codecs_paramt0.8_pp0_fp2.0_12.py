import codecs
codecs.register_error('strict', codecs.ignore_errors)

# For backwards compatibility and uniformity
from openlibrary.api import OpenLibrary

#
# Games
#

class Player:
    """A player of the game."""
    def __init__(self, name, points=0, history=None):
        self.name = name
        self.points = points
        if history is None:
            self.history = []
        else:
            self.history = history

    def __repr__(self):
        """Returns a string representation of the player."""
        return 'Player("%s", points=%d, history=%s)' % (self.name, self.points, self.history)

class Question:
    """A question in the game.

    Each question contains the text of the question and all the answers
    with their correctness status.

    """
    def __init__(self, text, answers):
        self.text = text
        self.answers = answers

    def __repr__(self):
        """Returns a string representation of the question."""
       
