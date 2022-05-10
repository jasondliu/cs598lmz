import socket
# Test socket.if_indextoname(), socket.socket.fileno(self)

def test_indextoname(devname):
    try:
        ifindex = socket.if_nametoindex(devname)
    except socket.error:
        print(socket.if_nametoindex.__name__, 'failed for interface', devname)
        return
    try:
        ifname = socket.if_indextoname(ifindex)
    except socket.error as msg:
        print(msg)
        return
    finally:
        print('%s: %s, %s' % (devname, ifindex, ifname))

def test_fileno(socket):
    try:
        print('%s: %s' % (
            socket.fileno.__name__, socket.fileno()))
    except socket.error as msg:
        print(msg)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 5005))
    devname = sock.getsockname()[0
