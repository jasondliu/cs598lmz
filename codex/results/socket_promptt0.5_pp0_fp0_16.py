import socket
# Test socket.if_indextoname() for IPv4 and IPv6

def test(family, socktype, proto, canonname, sa):
    print('family:', family, 'type:', socktype, 'proto:', proto,
          'canonname:', canonname, 'sa:', sa)
    try:
        name = socket.if_indextoname(sa[9])
        print('if_indextoname:', name)
        if name != canonname:
            print('ERROR: indextoname returned', name, 'instead of', canonname)
    except Exception as msg:
        print('ERROR: if_indextoname failed:', msg)


def get_ipv4_addresses():
    """Yields a tuple of (family, socktype, proto, canonname, sa) for each
    IPv4 address."""
    for info in socket.getaddrinfo(None, None, socket.AF_INET,
                                   socket.SOCK_DGRAM, socket.IPPROTO_UDP,
                                   socket.AI_PASSIVE):
        yield info


def get
