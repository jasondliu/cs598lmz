import gc, weakref
import struct, sys
from fcntl import ioctl
from os import open, O_RDWR, O_SYNC
from select import select
from termios import B115200, B230400, B460800, B921600, TCSANOW, tcflush, tcsetattr, cfsetspeed, error as termios_error
from time import time
from traceback import format_exc
from array import array

from can.message import Message
from can.interfaces.interface import Bus
from .socketcan_constants import *

if platform == "linux" or platform == "linux2":
    import fcntl

def CANFD_MTU(base_mtu):
    return base_mtu + CANFD_MTU_DIFF

class SocketcanBus(Bus):
    """
    SocketcanBus represents a virtual CAN "bus", and maintains a
    list of all the connected interfaces.

    It is a subclass of :class:`can.BusABC`.

    :param int base_mtu: Maximum Transmission Unit (MTU) of a classic CAN frame

        .. note::
