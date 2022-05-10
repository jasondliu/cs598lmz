import socket
# Test socket.if_indextoname()

def if_indextoname(ifindex):
    """
    if_indextoname(ifindex) -> string

    Return the name of an interface, given its index.
    """
    if not isinstance(ifindex, int):
        raise TypeError("an integer is required")
    try:
        return socket.if_indextoname(ifindex)
    except OSError as err:
        if err.args[0] != errno.EINVAL:
            raise
        raise ValueError("invalid if_index")

def test_if_indextoname():
    # Test invalid ifindex
    try:
        if_indextoname(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid if_index not detected")

    # Test valid ifindex
    ifname = if_indextoname(1)
    if not ifname:
        raise AssertionError("if_indextoname() returned empty string")

