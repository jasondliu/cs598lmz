import socket
import time

# Define some constants from the socket module
# these are necessary for setting the time to live
# on the packets
SOL_SOCKET = socket.SOL_SOCKET
SO_SNDBUF = socket.SO_SNDBUF
SO_RCVBUF = socket.SO_RCVBUF

# Some constants used for the algorithm
MAX_TIME = 8
TIMEOUT = 0.1
TTL = 20

# The size of the packets used in the algorithm
# It is important that the packets are of exact
# size. Size is in Bytes
PACKET_SIZE = 1500

# The number of packets sent to the destination
# The size of the file will then be
# PACKET_SIZE * NUMBER_OF_PACKETS
NUMBER_OF_PACKETS = 200

def simple_size(addr, port=80):
    """
    Finds the bandwidth between the client and
    the server using a simple algorithm.

    addr :    str, the address of the server.
    
    port :    int, optional, the port used by
