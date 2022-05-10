import socket
socket.if_indextoname(3)

# Open an address file.
# The 'wb' states to use binary write permissions.
testFile = open("127.0.0.1.bin", 'wb')

# Add the IP address to the file.
testFile.write(socket.inet_aton("127.0.0.1"))

# Close the file.
testFile.close()
