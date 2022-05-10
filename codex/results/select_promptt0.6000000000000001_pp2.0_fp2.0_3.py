import select
# Test select.select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind(("localhost", 8002))
server.listen(10)

inputs = [server]
outputs = []

while True:
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            connection.setblocking(0)
            inputs.append(connection)
        else:
            data = s.recv(1024)
            if data:
                s.send(data)
            else:
                s.close()
                inputs.remove(s)
    for s in writeable:
        try:
            next_msg = message_queues[s].get_nowait()
        except Queue.Empty:
            outputs.remove(s)
        else:
            s.send(next_msg)
    for s in exceptional:
        inputs.remove(s)
        if
