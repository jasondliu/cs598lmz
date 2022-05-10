import select
import socket
import sys
import threading
import time

import serial

from . import __version__, config, utils

__all__ = ['RemoteServer']


class RemoteServer:
    """RemoteServer class.

    This class implements a remote server that can be used to execute
    commands on a remote machine.

    The server can be used with a serial port (e.g. for debug output over
    JTAG) or a network socket (e.g. for debug output over Ethernet).

    The server commands can be defined by the user in a subclass of
    this class.

    """

    # pylint: disable=too-many-instance-attributes, too-many-public-methods
    # pylint: disable=too-many-arguments, too-many-branches, too-many-locals
