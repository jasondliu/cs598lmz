import socket
# Test socket.if_indextoname()

import socket, os

def main():
    if os.name == 'nt':
        print("skipping test on Windows")
        return
    print("testing socket.if_indextoname()")
    ifname = socket.if_indextoname(1)
    print("interface name: %s" % ifname)

if __name__ == '__main__':
    main()
