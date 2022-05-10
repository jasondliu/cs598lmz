import socket
# Test socket.if_indextoname()

# Test the function with a valid index
if_name = socket.if_indextoname(1)
print("Interface name:", if_name)

# Test the function with an invalid index
if_name = socket.if_indextoname(100)
print("Interface name:", if_name)
