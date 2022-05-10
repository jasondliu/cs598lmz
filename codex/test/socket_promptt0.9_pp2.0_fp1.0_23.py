import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))

def get_hostname():
    return socket.gethostbyaddr(socket.gethostname())[0]

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = socket.gethostname()
    s.connect((hostname, 0))
    return s.getsockname()[0]

def get_mac_address(ifname='eth0'):
    """
    Get mac address from a specified interface name (e.g. eth0).

    Return: mac address as a string or None.

    Note:
        This function works by calling SIOCGIFHWADDR which
        is a Linux-specific ioctl and therefore it is Linux-specific.
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
