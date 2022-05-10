import select
# Test select.select()

import socket
import time

# Create a nonblocking UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setblocking(0)

# Listen for packets on port 50000
s.bind(('', 50000))

while True:
    # Wait for data to be available on the socket
    ready = select.select([s], [], [], 1.0)
    if ready[0]:
        data, addr = s.recvfrom(1024)
