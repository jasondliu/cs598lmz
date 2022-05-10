import select
from multiprocessing import Process
from signal import SIGINT, signal

from . import config


def read_from_socket(socket, queue):
    """Read from a socket and put the message on the queue."""
    while True:
        try:
            message = socket.recv()
            queue.put(message)
        except zmq.error.ZMQError:
            # There is no message waiting
            pass


def serve(server_port, client_port, queue):
    """Run the server.

    The server will listen on the socket with address server_port. All
    messages received on this socket will be put on the queue. The server
    will also listen on the socket with address client_port. All messages
    on this socket will be sent to all connected clients.
    """
    # Create context
    context = zmq.Context()

    # Create the server socket
    server = context.socket(zmq.REP)
    server.bind('tcp://*:{}'.format(server_port))

    # Create the client socket
    clients = context.
