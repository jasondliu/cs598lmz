import socket
# Test socket.if_indextoname()

# TODO(pts): Test socket.if_indextoname() a bit more.
#            It is probably not implemented on Windows.

def test_if_indextoname():
    """Test socket.if_indextoname()."""
    for if_index in range(256):
        try:
            # Get name and index of the interface with index if_index.
            if_name = socket.if_indextoname(if_index)
            if if_name is None:
                continue  # Skip this interface.
            if_index2 = socket.if_nametoindex(if_name)
        except socket.error:
            continue
        # Test if_nametoindex() and if_indextoname() on the interface if_index.
        assert if_index2 == if_index, ('if_name2if_index=%r if_index=%r' %
                                       (if_index2, if_index))
