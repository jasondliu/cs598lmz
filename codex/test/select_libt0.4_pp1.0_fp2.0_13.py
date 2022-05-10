import select
import socket
import sys
import threading
import time

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 client.py <hostname> <port>")
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (host, port)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    # Create a thread to listen for incoming messages
    t = threading.Thread(target=listen, args=(sock,))
    t.start()

    # Send messages
    while True:
        msg = input()
        sock.send(msg.encode())

