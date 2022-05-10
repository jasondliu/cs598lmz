import socket
import struct
import sys
import time

# IP address of the destination
IP = '10.0.0.1'

# Port number of the service
PORT = 80

# Initial sequence number
start_seq = 0

# Maximum sequence number
max_seq = 0

# threshhold for re-transmission
threshold = 1

# timeout for re-transmission
timeout = 0.1

# maximum sequence number of the received ACKs
max_ack = 0

# maximum congestion window size
MAX_CWND = 50

# initial congestion window size
cwnd = 1
# slow start threshold
ssthresh = 15


# This method receives an acknowledgement from the receiver
# @param: socket - socket over which the acknowledgements will be received
# @return: tuple containing the acknowledgement number and the sequence number
