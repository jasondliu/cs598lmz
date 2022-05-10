import weakref

from . import (
    base,
    device,
    group,
    port,
    queue,
    flow,
    meter,
    table,
    statistics,
    util,
)
from . import error
from .error import *
from .log import *


class SwitchConnection(base.ConnectionBase):
    """
    Implementation of a switch connection.

    The switch connection is a high-level API that provides access to
    the switch features.
    """

    def __init__(self, dp, addr,
                 socket_family=socket.AF_UNIX,
                 socket_type=socket.SOCK_STREAM):
        """
        Initialize a switch connection.

        Args:
            dp (ryu.controller.controller.Datapath): The datapath object.
            addr (tuple): Address of the switch.
            socket_family (int): Socket family.
            socket_type (int): Socket type.
        """
        super(SwitchConnection, self).__init__(
            dp, addr, socket_family, socket_type)


