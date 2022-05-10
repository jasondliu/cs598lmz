import socket
# Test socket.if_indextoname()
import optparse

def if_indextoname(ifindex):
    """Translate an interface index to a name.
    @arg ifindex: An interface index.
    @return: The name of the corresponding interface.
    """
    return socket.if_indextoname(ifindex)

def main():
    parser = optparse.OptionParser()
    parser.add_option("-n", "--number", dest="number",
           action="store", type="int", default=1,
           help="number of rounds")
    parser.add_option("-p", "--port", dest="port",
           action="store", type="int", default=9000,
           help="port number")
    (options, args) = parser.parse_args()

    for i in range(options.number):
        print 'round %d' %i
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
