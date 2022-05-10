import socket
# Test socket.if_indextoname()

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if_index = s.if_nametoindex("lo")
print("lo index:", if_index)

if_name = s.if_indextoname(if_index)
print("lo name:", if_name)
