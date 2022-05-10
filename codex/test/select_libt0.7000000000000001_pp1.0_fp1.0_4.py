import selectors
import socket
import time
import json


# Configure the server's IP and PORT
PORT = 8080
IP = "212.128.253.64"
MAX_OPEN_REQUESTS = 5

sel = selectors.DefaultSelector()


def process_request(conn, addr):
    """Process the request received.

    Parameters: 
        addr: Address of the client.
    """

    print(f"\nAttending connections from client: {addr}")

    # Read the message from the client
    msg = conn.recv(2048).decode()
    print(msg)


    if len(msg) > 0:
        msg = msg.split('\n')[0]
        msg = msg.split(' ')[1]
        print(msg)
        if msg == "/":
            filename = "index.html"

        elif msg == "/blue":
            filename = "blue.html"

        elif msg == "/pink":
            filename = "pink.html"

