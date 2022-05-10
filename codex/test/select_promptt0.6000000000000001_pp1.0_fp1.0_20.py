import select
# Test select.select() by using it to implement a simple
# interactive echo server.

def echo_server(port, bufsize=1024):
    # Create and bind a listening socket
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind(('', port))
    lsock.listen(5)
    print('listening on port %d' % port)

    # Outgoing socket list
    clients = []

    while True:
        # Call select to get ready sockets
        rsocks, wsocks, esocks = select.select([lsock] + clients, [], [])

        # Service sockets ready for reading
        for sock in rsocks:
            if sock is lsock:
                # Incoming connection: add it to clients
                conn, addr = lsock.accept()
                print('connection from %s' % repr(addr))
                clients.append(conn)
            else:
                # Outgoing connection: service it
                data = sock.recv(bufsize)
