import socket
import sys

def print_usage():
    print """Usage: python client.py [host] [port]
Example: python client.py localhost 9999
"""

def main(args):
    if len(args) != 3:
        print_usage()
        return 1

    host = args[1]
    port = int(args[2])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    try:
        while True:
            data = sock.recv(1024)
            if data:
                print 'Received: %s' % data
            else:
                print 'Connection closed by server'
                break

    finally:
        sock.close()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
