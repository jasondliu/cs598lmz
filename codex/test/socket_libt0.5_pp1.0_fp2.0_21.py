import socket
import sys

def main(argv):
    if len(argv) != 2:
        print("Usage: ./client.py <hostname> <port>")
        sys.exit(2)

    hostname = argv[0]
    port = int(argv[1])

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (hostname, port)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

