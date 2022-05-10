import socket
# Test socket.if_indextoname()

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get the index of the interface
index = s.if_nametoindex('lo')

# Get the name of the interface
name = s.if_indextoname(index)

# Print the index and name
print(index, name)

# Close the socket
s.close()
