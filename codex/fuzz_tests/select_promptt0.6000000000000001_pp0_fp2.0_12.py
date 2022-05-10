import select
# Test select.select()

# Register the socket to monitor
rlist, wlist, xlist = select.select([server] , [], [])

# Monitor the socket until it's readable
while not rlist:
    rlist, wlist, xlist = select.select([server], [], [])

# Accept a connection
connection, client_address = server.accept()

# Receive the data in small chunks and retransmit it
while True:
    data = connection.recv(16)
    print('received "%s"' % data)
    if data:
        print('sending data back to the client')
        connection.sendall(data)
    else:
        print('no more data from', client_address)
        break

# Clean up the connection
connection.close()

# 10.5.5 Closing the server
# When the server is no longer needed, call its shutdown() method.

# Stop listening for incoming connections
server.shutdown(socket.SHUT_RDWR)

# Close the socket
server.close()
