import _struct
import _socket
import _ssl
import _io


def _set_default_timeout(timeout):
    """Set default timeout for socket."""
    _socket.setdefaulttimeout(timeout)


def _get_default_timeout():
    """Get default timeout for socket."""
    return _socket.getdefaulttimeout()


def _create_unix_socket(address):
    """Create a Unix domain socket."""
    return _socket.socket(_socket.AF_UNIX, _socket.SOCK_STREAM)


def _create_tcp_socket(address):
    """Create a TCP socket."""
    return _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)


def _create_socket(address):
    """Create a socket."""
    if address[0] == _socket.AF_UNIX:
        return _create_unix_socket(address)
    elif address[0] == _socket.AF_INET:
        return _create_tcp_socket(address)
