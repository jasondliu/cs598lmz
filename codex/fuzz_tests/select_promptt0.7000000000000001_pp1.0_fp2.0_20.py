import select
# Test select.select() behaviour in the case of ECONNRESET

import errno
import socket

# Create a socket pair for testing.
listener = socket.socket()
listener.bind(('127.0.0.1', 0))
listener.listen(1)
acceptor = socket.socket()
acceptor.connect(listener.getsockname())

# Create a new thread in which the listener will accept and close the
# connection.
def accept_and_close():
    while True:
        try:
            conn, addr = listener.accept()
            conn.close()
        except socket.timeout:
            break

# Set up the listener to time out after a second.
listener.settimeout(1.0)
# Start the accept-and-close thread.
import thread
thread.start_new_thread(accept_and_close, ())
# Wait for the connection to be accepted and closed.
while True:
    try:
        select.select([acceptor], [], [], 1.0)
        break
    except socket.error, e:
        if e
