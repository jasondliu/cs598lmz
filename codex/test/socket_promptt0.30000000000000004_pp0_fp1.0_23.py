import socket
# Test socket.if_indextoname()

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get the interface index
index = s.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, "eth0")

# Convert the index to a name
name = socket.if_indextoname(index)

# Print the name
print(name)

# Close the socket
s.close()
