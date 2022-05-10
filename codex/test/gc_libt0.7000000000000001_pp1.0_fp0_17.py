import gc, weakref
import sys

# This module is the real main module of the game, but we import it as game
# This is because we want to be able to run the game from a different module
# without it closing when the game exits.
# This way we can run the game from the editor, and it will not close
# when we open the game.

