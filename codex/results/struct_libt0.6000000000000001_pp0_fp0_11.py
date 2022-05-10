import _struct

#####################
#       Flags       #
#####################

# Flag values for the options field

# Node is a leaf
L = 1
# Node has an associated value
V = 2

#####################
#     Functions     #
#####################

def _pack(data):
    """
    Pack data into a bytes object
    """
    if isinstance(data, bytes):
        return data
    elif isinstance(data, str):
        return data.encode()
    elif isinstance(data, int):
        return struct.pack('<I', data)
    else:
        raise ValueError("Could not pack data")

def _unpack(data):
    """
    Unpack data from a bytes object
    """
    if isinstance(data, bytes):
        return data.decode()
    elif isinstance(data, str):
        return data
    elif isinstance(data, int):
        return struct.unpack('<I', data)[0]
    else:
        raise ValueError("Could not unpack data")


