import socket
# Test socket.if_indextoname
if_indextoname = socket.if_indextoname
error = socket.error

interface_id = if_indextoname(1)

#interface_id should not equal None.
#TODO: Is there a better way to check for existence of name?
if interface_id is None or interface_id == " ":
    print("Interface not found")
else:
    print(interface_id)
