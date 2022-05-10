import select
import socket
import sys
import types
import tty


def get_connected_client():
    client, address = server_socket.accept()
    print('Connected to ', address)

    # Make input non-blocking
    client.setblocking(0)

    # Add client to selectors
    sel.register(client, selectors.EVENT_READ, read)
    return client


def read(connection, mask):
    global client
    global server_socket

    data = connection.recv(1024)
    if data:
        # Send data to stdout
        sys.stdout.buffer.write(data)
        sys.stdout.buffer.flush()

        # Send data to client
        if client:
            client.send(data)
    else:
        # Close connection
        print('Closing connection')
        sel.unregister(connection)
        connection.close()

        # Try to accept new connection
        client = get_connected_client()


if len(sys.argv) != 3:
    print('usage:', sys.argv[
