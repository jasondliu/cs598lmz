import socket
import struct
import sys

from threading import Thread
from time import sleep

from packet import Packet

# global variables
g_sequence_number = 0
g_max_sequence_number = 2 ** 32
g_send_window = 10
g_timeout = 1


class Sender(Thread):
    """
    Sender class.
    """

    def __init__(self, filename, socket, ip_address, port, window_size, timeout, congestion_window_size,
                 select_timeout):
        """
        Constructor.
        :param filename: name of the file to be sent
        :param socket: the socket that is used to send the file
        :param ip_address: the receiver's ip address
        :param port: the receiver's port
        :param window_size: the window size for the go-back-n protocol
        :param timeout: the timeout for the go-back-n protocol
        :param congestion_window_size: the maximum congestion window size
        :param select_timeout: the time we allow select() to wait for receiving an ack before timing out

