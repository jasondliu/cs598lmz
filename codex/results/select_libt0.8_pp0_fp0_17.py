import selectors
import socket
import types

mysel = selectors.DefaultSelector()
keep_running = True


def read(connection, mask):
    global keep_running
    client_address = connection.getpeername()
    print("read ({})".format(client_address))
    data = connection.recv(1024)
    if data:
        # A readable client socket has data
        print(" received {!r} from {}".format(data, client_address))
        connection.sendall(data)
    else:
        # Interpret empty result as closed connection
        print(" closing from {}".format(client_address))
        mysel.unregister(connection)
        connection.close()
        # Tell the main loop to stop
        keep_running = False



server_address = ('localhost', 10000)
print("starting up on {} port {}".format(*server_address))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
