import socket
# Test socket.if_indextoname()

import socket
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: if_indextoname.py interface_index')
        sys.exit(2)

    interface_index = int(sys.argv[1])
    try:
        interface_name = socket.if_indextoname(interface_index)
    except ValueError as err:
        print('ERROR: %s' % str(err))
    else:
        print('%s is interface %d' % (interface_name, interface_index))
