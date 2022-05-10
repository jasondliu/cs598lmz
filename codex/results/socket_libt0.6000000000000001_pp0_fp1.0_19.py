import socket
import sys
import time
from threading import Thread


def get_ip():
    """
    Get the IP address of the host machine.

    :return: string: IP address
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


class Server:
    """
    Server class.
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = {}  # client socket: client name

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_
