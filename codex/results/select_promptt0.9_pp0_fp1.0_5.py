import select
# Test select.select function
# Run this program and open a new terminal
# Use command "nc -l 7777" to liston port 7777
import queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(('localhost', 5555))
server.listen(5)

msg_queue = {}

inputs = [server]
outputs = []
message_queues = {}
timeout = 20

while inputs:
    readable, writable, exceptional = select.select(
        inputs, outputs, inputs, timeout)

    # When timeout reached, select return three empty lists
    if not (readable or writable or exceptional):
        print("Time out ! ")
        break
    for s in readable:
        if s is server:
            # A "readable" socket is ready to accept a connection
            connection, client_address = s.accept()
            print("    connection from", client_address)
            connection.setblocking(0)
            inputs.append(connection)

            # Give the connection a queue for data
