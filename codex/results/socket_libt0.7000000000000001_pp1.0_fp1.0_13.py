import socket
import sys
import time
import inotify.adapters

if __name__ == '__main__':
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = ('localhost', 10000)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)

    try:
        i = inotify.adapters.Inotify()
        i.add_watch('/tmp')
        for event in i.event_gen():
            if event is not None:
                (header, type_names, watch_path, filename) = event
                print type_names
                if 'IN_CREATE' in type_names:
                    print type_names
                    print watch_path
                    print filename
    finally:
        sock.close()
