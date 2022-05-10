import select
# Test select.select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
server.setblocking(0)
server.bind(('localhost', 50000))
server.listen(1)

connections = {}
readers = [server]
writers = []

while readers:
    readable, writable, exceptional = select.select(readers, writers, readers)

    for s in readable:
        if s is server:
            connection, peer = s.accept()
            print 'New connection from {}'.format(peer)
            connection.setblocking(0)
            connections[connection] = peer
            readers.append(connection)
        else:
            data = s.recv(1024)
            if data:
                print '{} sent {}'.format(connections[s], data)
                writers.append(s)
            else:
                print 'Closing {}'.format(connections[s])
                readers.remove(s)

