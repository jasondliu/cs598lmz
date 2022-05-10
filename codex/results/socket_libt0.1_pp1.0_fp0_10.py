import socket
import sys
import time
import threading
import os
import signal
import subprocess
import re

# Global variables

# The port on which to listen
listenPort = 12000

# The socket on which to listen
listenSocket = None

# The socket on which to send
sendSocket = None

# The socket on which to receive
receiveSocket = None

# The socket on which to receive
receiveSocket2 = None

# The socket on which to receive
receiveSocket3 = None

# The socket on which to receive
receiveSocket4 = None

# The socket on which to receive
receiveSocket5 = None

# The socket on which to receive
receiveSocket6 = None

# The socket on which to receive
receiveSocket7 = None

# The socket on which to receive
receiveSocket8 = None

# The socket on which to receive
receiveSocket9 = None

# The socket on which to receive
receiveSocket10 = None

# The socket on which to receive
receiveSocket11 = None

# The socket on which
