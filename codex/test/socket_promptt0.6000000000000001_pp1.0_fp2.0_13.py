import socket
# Test socket.if_indextoname()

def get_if_index(ifname):
    return socket.if_indextoname(socket.if_nametoindex(ifname))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: %s <ifname>\n" % sys.argv[0])
        sys.exit(1)

    ifname = sys.argv[1]
    ifindex = get_if_index(ifname)
    print("ifname %s -> ifindex %s" % (ifname, ifindex))
