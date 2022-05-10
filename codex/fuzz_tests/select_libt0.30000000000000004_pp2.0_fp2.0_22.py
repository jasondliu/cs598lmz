import select
import sys
import time

#-------------------------------------------------------------------------------

def main(argv):
    if len(argv) != 2:
        print 'usage: %s <port>' % argv[0]
        sys.exit(1)

    port = int(argv[1])

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', port))
    server.listen(5)
    server.setblocking(0)

    inputs = [server]
    outputs = []
    message_queues = {}

    while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)

        for s in readable:
            if s is server:
                connection, client_address = s.accept()
                print 'new connection from', client_address
                connection.setblocking(0)
                inputs.append(connection)
                message_queues[connection] =
