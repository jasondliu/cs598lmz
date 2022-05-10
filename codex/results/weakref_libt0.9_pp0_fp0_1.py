import weakref
from . import net as simnet
from .pyarx import Arx


def construct_name(active, player, idnum):
    if active:
        name = "Active "
    else:
        name = "Inactive "
    name += player
    name += " "
    name += str(idnum)
    return name


class PlayerActor(Actor):
    def __init__(self, **kwargs):
        super(PlayerActor, self).__init__(**kwargs)

        self.add_behavior(simnet.connection.ConnectionBehavior())


class PlayerObserver(Observer):
    def __init__(self):
        super(PlayerObserver, self).__init__()


class Player(object):
    """
    The Player class is a wrapper around a PlayerActor and PlayerObserver,
    creating a "player" of a game.  Each Player is either "active" or
    "inactive" and has a unique name.  An active Player has privileges to
    call reset() on the Arx instance and set valid_inputs since it is
    considered
