import socket
import struct

from . import exceptions
from . import utils
from . import packet

from .packet import Packet, PacketType
from .exceptions import PacketException
from .utils import unpack_data, pack_data, read_data, write_data

from .protocol import Protocol, ProtocolState, ProtocolStateType
from .protocol import ProtocolException, ProtocolStateException

from .protocol.packet import PacketProtocol, PacketProtocolState, PacketProtocolStateType
from .protocol.packet import PacketProtocolException, PacketProtocolStateException


class PacketConnectionProtocol(Protocol):
    """
    The PacketConnectionProtocol class is the base class for all packet-based connection protocols.

    :param connection: The connection to use.
    :type connection: Connection
    :param protocol: The protocol to use.
    :type protocol: Protocol
    :param on_packet_received: The on packet received callback.
    :param on_packet_sent: The on packet sent callback.
    :param on_packet_received_
