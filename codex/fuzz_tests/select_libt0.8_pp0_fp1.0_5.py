import selectors
import socket
import logging


# Need to get data from a webpage.
# We start by opening up a socket.
# We need to open a socket to a webpage
# (this is basically a connection to a webpage).

def get_socket():
    """
    Get a socket connection to a webpage.

    :return: Returns
             (socket, host, port)
             where socket is the socket connection
             host and port are the host and port used
             to connect the socket.
    """

    # Selector is a tool used for selecting a socket.
    # It can select multiple sockets at once.
    selector = selectors.DefaultSelector()

    # Creates an IPV4 TCP socket.
    # You can also create an IPV4 UDP socket
    # by using socket.SOCK_DGRAM instead.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # A socket object is not ready to be used until it is located
    # ("bound") to a port on a host.
    # The difference between a socket and a socket object
