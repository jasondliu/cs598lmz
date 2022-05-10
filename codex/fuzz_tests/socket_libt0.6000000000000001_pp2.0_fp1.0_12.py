import socket
import threading
import time
import json
import os
import datetime
import sys

# The following are server settings.
# This is the server's IP address. This should be the
# IP address of the machine the server is running on.
# If you are running the server and client on the same
# machine, then localhost (i.e. 127.0.0.1) will work.
# If you are running the server and client on different
# machines, then you should put in the IP address of the
# machine that is running the server.
HOST = 'localhost'

# This is the port number that the server will listen on.
# It can be any number you want, but it must be the same
# as the port number the client uses.
PORT = 8080

# This is the maximum number of queued connections we will allow
BACKLOG = 50

# This is the buffer size of each message.
# It is generally a good idea to make this a power of two.
BUFFERSIZE = 1024

# This is the list of connected clients.
# It starts off empty.
cl
