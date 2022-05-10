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

