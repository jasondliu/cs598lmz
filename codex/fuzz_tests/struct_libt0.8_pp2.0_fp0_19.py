import _struct

try:
    xrange
except NameError:
    xrange = range

# The packet template
#  http://tools.ietf.org/html/rfc768

UDP_HEADER_LENGTH = 8

# socket.inet_pton
def inet_pton(address_family, ip_string):
    """
    Converts an IP address from string format to binary format
    """
    if address_family == socket.AF_INET:
        return socket.inet_aton(ip_string)
    elif address_family == socket.AF_INET6:
        if '.' in ip_string:  # a v4 addr
            v4 = socket.inet_aton(ip_string)
            v4map = '\x00' * 10 + '\xff\xff' + v4
            return v4map
        dbyts = [0] * 8   # 8 groups
        grps = ip_string.split(':')
        for i, v in enumerate(grps):
            if v:
                dbyts[i] = int
