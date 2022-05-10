import socket
# Test socket.if_indextoname()
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: if_indextoname.py <interface index>')
        sys.exit(1)

    index = int(sys.argv[1])
    ifname = socket.if_indextoname(index)
    if ifname:
        print('{} = {}'.format(index, ifname))
    else:
        print('{} is not a valid interface index'.format(index))
