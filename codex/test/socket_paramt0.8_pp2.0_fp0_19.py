import socket
socket.if_indextoname("2")

# Just for convenience: A name to address dictionary for socket.inet_aton
address_dict = {
    "localhost": "127.0.0.1",
    "google.com": socket.gethostbyname("google.com")
}


def bin_to_int(bin):
    """Convert a binary string to an integer."""
    return int(bin, 2)


def int_to_bin(n):
    """Convert an integer to a binary string."""
    return bin(n)[2:]


def int_to_hex(n):
    """Convert an integer to a hexadecimal string."""
    return hex(n).replace("0x", "")


def hex_to_int(hex):
    """Convert a hexadecimal string to an integer."""
    return int(hex, 16)


def bin_to_hex(bin):
    """Convert a binary string to a hexadecimal string."""
    return int_to_hex(bin_to_int(bin))


