import select
# Test select.select

import select
import socket
import time

# Wait for at most 1 second for a "socket ready" event.
ready = select.select([socket.socket()], [], [], 1.0)
print ready
if not ready[0]:
    print "Timed out."

# Wait for at most 2 seconds for a "socket ready" event.
ready = select.select([socket.socket()], [], [], 2.0)
print ready
if not ready[0]:
    print "Timed out."

# Wait for at most 3 seconds for a "socket ready" event.
ready = select.select([socket.socket()], [], [], 3.0)
print ready
if not ready[0]:
    print "Timed out."

# Wait for at most 4 seconds for a "socket ready" event.
ready = select.select([socket.socket()], [], [], 4.0)
print ready
if not ready[0]:
    print "Timed out."

# Wait for at most 5 seconds for a "socket ready" event.
ready = select.select([socket
