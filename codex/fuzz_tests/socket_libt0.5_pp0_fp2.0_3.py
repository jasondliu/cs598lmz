import socket
import csv
import time
import os
import sys
import getpass

# This script is designed to be run on a Raspberry Pi with a Sense HAT.
# It will collect data from the attached Sense HAT and send it to a
# remote server via UDP.

# This script will run until it is manually terminated.

#
# Constants
#

# The IP address of the remote server to send data to.
SERVER_IP = '192.168.1.1'

# The port to send data to on the remote server.
SERVER_PORT = 5005

# How often to collect data, in seconds.
DATA_COLLECTION_INTERVAL = 1

# The location to write the CSV file to.
OUTPUT_FILE = 'data.csv'

#
# Global variables
#

# The socket used to send data to the remote server.
sock = None

# The file used to write the CSV file to.
output_file = None

#
# Functions
#

def open_socket():
    '''
    Open the socket used to
