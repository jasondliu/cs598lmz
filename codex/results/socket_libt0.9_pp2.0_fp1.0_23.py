import socket

from .interface import Interface

class SSDP_UDP_Interface(Interface):
    """Class for SSDP UDP Interface
    UDP allows sending and listening on the same connection.
    """
    def __set_up_socket(self, port, bind=False):
        self.socket_address = ('', port)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # TCP_NODELAY necessary because each packet is independent of the other,
        # so there is no point in buffering and reorganizing them
        self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        self.socket.settimeout(self.SO_TIMEOUT)

        if bind:
            self.socket.bind(self.socket_address)

    def __init__(self, connection_handler, port=0, bind=False):
        super().
