import _struct

PROTO_FAMILY = {
    socket.AF_INET: 'AF_INET',
    socket.AF_INET6: 'AF_INET6',
}

PROTO_TYPE = {
    socket.SOCK_STREAM: 'SOCK_STREAM',
    socket.SOCK_DGRAM: 'SOCK_DGRAM',
}

PROTO_PROTOCOL = {
    socket.IPPROTO_IP: 'IPPROTO_IP',
    socket.IPPROTO_UDP: 'IPPROTO_UDP',
    socket.IPPROTO_TCP: 'IPPROTO_TCP',
}

_IF_NAMESIZE = 16
_IFREQ_SIZE = _IF_NAMESIZE + _struct.calcsize('=HI')


def get_if_list():
    """A wrapper around socket.if_nameindex() to return just the interface
    names as a list.

    @rtype: list(str)
    """
    return [s[0] for s in socket.if_
