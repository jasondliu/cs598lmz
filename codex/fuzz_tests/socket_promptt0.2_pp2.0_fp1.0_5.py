import socket
# Test socket.if_indextoname()

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get the interface index
index = s.if_nametoindex('lo')

# Convert the index to a name
name = s.if_indextoname(index)

# Print the results
print('Interface index:', index)
print('Interface name:', name)
