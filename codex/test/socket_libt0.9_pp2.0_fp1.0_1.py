import socket
import struct
from time import time, sleep
from collections import deque
from .connection import Connection
from .shell import Shell, ShellReturned
from .parser import Packet, Parser, PacketTooShort, PacketParsingError, CommandPacket
from .exceptions import (
    InvalidPacketError, InvalidSocketPathError, InvalidSocket,
    OpenFileError, ShellUnavailableError
)


class CtlConnection(Connection):
    __slots__ = (
        '_socket', '_server_pid',
        '_connected', '_parser', '_buffer'
    )

    #: An iterable of all the unix sockets discovered in the :code:`/var/run/tor` directory
    socket_paths = (f"/var/run/tor/control{i:03d}-auth-cookie" for i in range(100))

    #: The maximum number of bytes to read at a time from the control connection
    buffer_size = 1024

