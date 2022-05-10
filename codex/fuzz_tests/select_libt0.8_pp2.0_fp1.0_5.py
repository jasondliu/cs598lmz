import select
import signal
import struct
import sys
import time
import traceback

from logging import debug, info, warn
from socket import socket

# Info about the current connection
server = None
server_socket = None

# Global lock for all access to the server object
GLOCK = threading.Lock()

# Address of the client
CLIENT_ADDRESS = None

# Sequence number for packets sent to the client
seq_number = None

# List of packets, in order, that have been sent to the client.
# This is used to maintain packet order while some packets are
# still being processed.
packet_queue = []

# Buffer for received packets
packet_buffer = b''

# Number of times we have seen a FIN packet
fin_count = 0

# Whether we are currently shutting down
SHUTTING_DOWN = False

# Time we last sent a packet to the client
last_packet_time = 0.0

def configure_logging(verbose):
    """Configure logging according to the given verbosity level."""
    if verbose:
        level
