import selectors
import socket
import sys
import traceback

mysel = selectors.DefaultSelector()
keep_running = True


def read(connection, mask):
    global keep_running

    client_address = connection.getpeername()
    print('read({})'.format(client_address))
    data = connection.recv(1024)

    if data:
        # A readable client socket has data
        print('  received {!r}'.format(data))
        connection.sendall(data)
    else:
        # Interpret empty result as closed connection
        print('  closing')
        mysel.unregister(connection)
        connection.close()
        # Tell the main loop to stop
        keep_running = False


def accept(sock, mask):
    new_connection, addr = sock.accept()
    print('accept({})'.format(addr))
    new_connection.setblocking(False)
    mysel.register(new_connection, selectors.EVENT_READ, read)


if len(sys.argv) != 3:
    print("usage
