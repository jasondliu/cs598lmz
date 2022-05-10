import socket
# Test socket.if_indextoname()
for if_index in range(10):
    try:
        if_name = socket.if_indextoname(if_index)
    except ValueError:
        if_name = None
