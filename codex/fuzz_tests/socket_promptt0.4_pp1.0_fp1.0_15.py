import socket
# Test socket.if_indextoname()

# Get the interface index for the loopback interface
loopback_index = socket.if_nametoindex('lo')

# Get the interface name for the loopback interface
loopback_name = socket.if_indextoname(loopback_index)

# Display the interface index and name
print(f'The loopback interface has index {loopback_index} and name {loopback_name}')

# Get the interface index for the first non-loopback interface
first_if_index = socket.if_nametoindex('eth0')

# Get the interface name for the first non-loopback interface
first_if_name = socket.if_indextoname(first_if_index)

# Display the interface index and name
print(f'The first non-loopback interface has index {first_if_index} and name {first_if_name}')
