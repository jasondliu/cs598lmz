import socket
import math
import binascii
import struct
import sys
import time
import datetime

#-------------------------------------------------------------------------------
# Global Variables
#-------------------------------------------------------------------------------

# The UDP port number to use
UDP_PORT_NUMBER = 2727

# The max size of a UDP packet
MAX_UDP_PACKET_SIZE = 65535

# The number of bytes in a single data packet
DATA_PACKET_SIZE = 512

# The number of bytes in a single header packet
HEADER_PACKET_SIZE = 1024

# The number of bytes in a single footer packet
FOOTER_PACKET_SIZE = 1024

#-------------------------------------------------------------------------------
# Function Definitions
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Function:    openUDPPort
#
# Description: This function opens a UDP port with the given port number.
#
# Parameters:  portNum - The UDP port number to open.
#
# Returns:     A socket that is bound to the given port number.
#-------------------------------------------------------------------------------
def openUDPPort(portNum):
    # Create a UDP socket
    sock =
