import select
# Test select.select()

# Use select() to poll for input on a socket, and for a timeout
# to occur.

import socket
import time

print "Starting at", time.time()

ready = select.select([socket.socket()], [], [], 5.0)

print "ready", ready
print "Ending at", time.time()

# Starting at 884455076.69
# ready ([], [], [])
# Ending at 884455081.69
