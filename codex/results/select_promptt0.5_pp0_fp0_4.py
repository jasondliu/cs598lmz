import select
# Test select.select()
#
# select() returns three lists of sockets: readable, writable, and exceptional.
#
# The readable list contains sockets that are ready for reading.
# The writable list contains sockets that are ready for writing.
# The exceptional list contains sockets that have raised exceptions.

import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(0)
    s.bind(('', 0))
    s.listen(5)

    # Get the port number.
    port = s.getsockname()[1]

    print('Listening on port {}'.format(port))

    # Wait for a connection.
    readable, writable, exceptional = select.select([s], [], [], 5.0)

    if readable:
        client, address = s.accept()
        print('Client connected from {}'.format(address))
    else:
        print('No client connected before the timeout.')

if __name__ == '__main__':
    main()
