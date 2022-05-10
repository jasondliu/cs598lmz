import select
# Test select.select for reading on a socket.
#
# Usage: python select_echo.py
#
# Start this program, then run select_echo_client.py a few times in
# separate windows.
#
# This sets up a server listening on port 25000. The client sends messages
# to the server, which sends them back to the client (echoing) and prints
# them out.
#
# This version uses select to wait until the socket is ready to read,
# instead of using recv with a 0 argument.
#
# Based closely on
# http://code.activestate.com/recipes/52558-logging-example-with-a-rotating-file-handler/
#
# This program is part of "Dive Into Python", a free Python book for
# experienced programmers.  Visit http://diveintopython.org/ for the
# latest version.

import socket
import select
import sys
import Queue

queue = Queue.Queue()

HOST = ''
PORT = 25000

# Create the server socket (to handle tcp requests using ipv4), make sure

