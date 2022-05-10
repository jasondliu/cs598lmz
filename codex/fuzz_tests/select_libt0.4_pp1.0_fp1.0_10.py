import select
import socket
import sys
import time
import threading
import Queue
import os

#-------------------------------------------------------------------------------
# Global constants
#-------------------------------------------------------------------------------

# The maximum number of bytes that can be sent in a single message.
MAX_MESSAGE_SIZE = 1024

# The maximum number of messages that can be queued for a single client.
MAX_MESSAGES_PER_CLIENT = 10

# The maximum number of bytes that can be queued for a single client.
MAX_BYTES_PER_CLIENT = MAX_MESSAGE_SIZE * MAX_MESSAGES_PER_CLIENT

# The maximum number of clients that can be connected at once.
MAX_CLIENTS = 10

# The maximum number of bytes that can be queued for all clients.
MAX_BYTES_TOTAL = MAX_BYTES_PER_CLIENT * MAX_CLIENTS

#-------------------------------------------------------------------------------
# Global variables
#-------------------------------------------------------------------------------

# The server's socket.
server_socket = None

# The list of connected clients.
clients = []

# The list
