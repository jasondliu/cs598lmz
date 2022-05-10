import select
import threading
import collections
import socket
import sys
import time
import re

# Packet related constants
PACKET_SIZE = 1500
MAX_PACKET_SIZE = 2048

# Timeout (in seconds)
TIMEOUT = 0.05

# Max number of retransmission attempts
MAX_RETRIES = 10

# Max number of packets to be outstanding at a given time
MAX_OUTSTANDING_PACKETS = 5

# Ack type constants
ACK = 0
NAK = 1

# Packet type constants
DATA = 0
EOF = 1

# TCP Header offsets
TYPE_OFFSET = 0
SEQ_OFFSET = 1
LEN_OFFSET = 5
DATA_OFFSET = 9

# TCP Header sizes
TYPE_SIZE = 1
SEQ_SIZE = 4
LEN_SIZE = 4

# File related constants
FILE_CHUNK_SIZE = 1024

# Other constants
BYTE_ORDER = 'big'

class TCPClient:

    def __init__(self, host, port, filename):
        self.host
