import select, socket, sys, queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address), file=sys.stderr)
server.bind(server_address)

server.listen(5)

inputs = [server]
outputs = []
message_queues = {}

while inputs:
    print('waiting for the next event', file=sys.stderr)
    readable, writable, exceptional = select.select(inputs, outputs, inputs)

    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            print('new connection from ', client_address, file=sys.stderr)
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = queue.Queue()
        else:
            data = s.recv(1024)
