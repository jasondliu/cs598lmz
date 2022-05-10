import _struct
import _libc

def _encode_window(window):
    """Encode a window size for use in the SOCKS4 protocol.

    :param window: The window size to encode.
    :returns: The encoded window size.
    """
    # The windows size is encoded in little endian, so we reverse the
    # bytes.
    return _struct.pack("<H", window)


def _encode_address(address):
    """Encode an address into the SOCKS4 format.

    :param address: The address to encode.
    :returns: The encoded address.
    """
    # If address is in the form of an IP address (four numbers
    # separated by dots), encode it as such -- a four-byte string in
    # network order.
    try:
        return _socket.inet_aton(address)
    except _socket.error:
        # Otherwise, we assume it's a hostname.  This is encoded as
        # a three-byte string, the first byte being a null-terminated
        # string.
        return _struct
