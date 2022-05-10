import socket
socket.if_indextoname(ni.fileno())

# Create a socket for incoming connections.
# No need to bind the socket before listening.
sys.stdout.write("%s\n"%("listening"))
listener=ILP.listener(port)

try:
    # Wait for a connection.
    connection=None
    while connection is None:
        connection, address = listener.accept()
        connection.settimeout(1)
    sys.stdout.write("New connection from %s\n"%(address))
    while True:
        try:
            input = connection.recv(20)
            sys.stdout.write("Received: %s\n"%(input))
        except socket.timeout:
            pass
except KeyboardInterrupt:
    sys.stderr.write("done\n")
    connection.close()
    listener.close()
    sys.exit(0)
