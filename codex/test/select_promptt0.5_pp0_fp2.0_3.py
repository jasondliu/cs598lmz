import select
# Test select.select

# Create a non-blocking socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(0)

# Connect to the server
sock.connect(("localhost", 10000))

# Set up a 10-second timeout
timeout = 10
endtime = time.time() + timeout

# Loop until we either have a successful connection or the timeout has passed
while True:
    # Do a select on the socket with a 1-second timeout
    r, w, e = select.select([sock], [sock], [sock], 1.0)

    # If the socket is readable, read some data
    if sock in r:
        data = sock.recv(4096)
        if data:
            print("Received:", data)
        else:
            print("Closing socket")
            sock.close()
            break

    # If the socket is writable, send some data
