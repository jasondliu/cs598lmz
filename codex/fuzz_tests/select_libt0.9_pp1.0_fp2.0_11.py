import select
import socket

from connection_components import ConnectionBuffer
from message_handler import MessageParser
from message_components import NetworkingMessageFactory
import protocol_commands as commands


SIZE_CONNECTION_BUFFER = 8192

BUFFER_PACKET_COMMAND = 1
BUFFER_PACKET_DATA = 2

BUFFER_PACKET_TYPES = {BUFFER_PACKET_COMMAND, BUFFER_PACKET_DATA}

PACKET_STATE_COMMAND = 0
PACKET_STATE_DATA_SIZE = 1


class BaseConnection(object):
    def __init__(self, socket):
        assert socket is not None and type(socket) == socket.socket
        super(BaseConnection, self).__init__()
        self._socket = socket

    @property
    def socket(self):
        return self._socket


class ServerConnection(BaseConnection):
    def __init__(self, server_socket, client_socket, on_client_read, client_buffer_size,
                 on_client_disconnected
