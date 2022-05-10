import select
# Test select.select

import select
import socket
import time

# Wait for at most 1 second for a "socket ready" event.
ready = select.select([socket.socket()], [], [], 1.0)
