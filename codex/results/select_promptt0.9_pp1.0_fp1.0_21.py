import select
# Test select.select
import socket
import random

print "connecting"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 10001))

# Wait 10 seconds for a response
to_read = [s]
to_write = []
has_quit = []

while to_read:
    read_ready, write_ready, except_ready = \
        select.select(to_read, to_write, [])
    # The first read_ready result should be the socket we listen on.
    for s in read_ready:
        # The socket might have data coming in 
        # Or, it might be ready to accept a connection,
        # in which case we will add it to the list.
        data = s.recv(8192)
        if data:
            print "Received:", data
        else:
            print "Closing socket"
            s.close()
            to_read.remove(s)
            # or has_quit.append(s)

    # Send data
    to_send
