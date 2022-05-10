import socket

from . import errors


def validate_host_name(host, port, family=socket.AF_UNSPEC):
    try:
        if family == socket.AF_UNSPEC:
            candidates = socket.getaddrinfo(host, port, family=socket.AF_INET)
            candidates += socket.getaddrinfo(host, port, family=socket.AF_INET6)
        else:
            candidates = socket.getaddrinfo(host, port, family=family)
    except socket.gaierror:
        raise errors.ErrHostnameInvalid(host)

    if not candidates:
        raise errors.ErrHostnameInvalid(host)

    return candidates
