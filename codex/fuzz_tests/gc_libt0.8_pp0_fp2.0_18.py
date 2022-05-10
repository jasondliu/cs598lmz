import gc, weakref


from engine import Engine
import config
import commands
from entities import Block, Drain, Trigger, Spawn
import logic

from twcommon.dowutil import BitList


class Game(object):
    """A blockworld game running on a server.

    This object encapsulates all of the state of a particular game.
    It has a corresponding GamePort object which is responsible for
    handling all of the network connections.

    FIXME: This object is starting to become too large, and should be divided
    into smaller pieces which are easier for me to follow.
    """
    # Configuration values.
    NAME = 'blockworld'
    WELCOME = 'Blockworld'
    HOST_IP = '127.0.0.1'
    PORT = 2222
    DEFAULT_MAP = 'default'
    DESCRIPTION = None

    # How often we run maintenance tasks.
    MAINT_INTERVAL = 1.0

    # How often we update the player's position to other clients.
    # This value is somewhat arbitrary, based on the responsiveness
    # that seems to work well for Blockworld.
   
