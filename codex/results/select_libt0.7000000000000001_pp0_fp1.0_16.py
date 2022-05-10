import select
import socket
import struct
import sys


def get_free_port():
    """Get a free port on localhost.

    Tries to find a free port on localhost by opening a socket on
    localhost without binding it.

    Returns:
        (int) : first free port found starting with 1024

    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    addr, port = s.getsockname()
    s.close()
    return port


def make_multipart_input(data):
    """Create a multipart/form-data body.

    Args:
        data (dict): form data

    Returns:
        (bytes) : multipart/form-data input

    """
    body = io.BytesIO()
    for key, value in data.items():
        body.write(b'--' + b'X'*16 + b'\r\n')
        body.write(b'Content-Disposition: form-data; name="' + key
