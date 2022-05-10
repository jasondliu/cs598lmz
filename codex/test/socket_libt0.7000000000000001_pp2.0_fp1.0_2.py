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

