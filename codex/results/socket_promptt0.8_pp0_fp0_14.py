import socket
# Test socket.if_indextoname()
print "if_indextoname(%d) = %s" % (9, socket.if_indextoname(9))

# Test socket.if_nametoindex()
print "if_nametoindex('lo') = %s" % (socket.if_nametoindex('lo'))

# Test socket.setdefaulttimeout()
print "setdefaulttimeout() before = %s" % (socket.getdefaulttimeout())
oldtimeout = socket.setdefaulttimeout(60)
print "setdefaulttimeout() after = %s" % (socket.getdefaulttimeout())
socket.setdefaulttimeout(oldtimeout)

"""


def get_socket_name(s=None):
    if s is None:
        s = socket.socket()
    return s.getsockname()

def get_timeout(s=None):
    if s is None:
        s = socket.socket()
    return s.gettimeout()


if __name__ == "__main__":
    s = socket.socket()
    print "if_indextoname(%d) = %
