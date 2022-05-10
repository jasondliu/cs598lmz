import socket
socket.if_indextoname(3)

# This is a function that will return the interface name given an index
# It will return None if the index is not valid
def get_interface_name(index):
    try:
        return socket.if_indextoname(index)
    except:
        return None

# This is a function that will return the interface index given a name
# It will return None if the name is not valid
def get_interface_index(name):
    try:
        return socket.if_nametoindex(name)
    except:
        return None

# This is a function that will return the interface index given a name
# It will return None if the name is not valid
def get_interface_index(name):
    try:
        return socket.if_nametoindex(name)
    except:
        return None

# This is a function that will return the interface MAC address given an index
# It will return None if the index is not valid
def get_interface_mac(index):
    try:
        s = socket.socket(socket.AF_PACKET, socket.SOCK
