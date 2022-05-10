import select
# Test select.select
import socket
import time

def test_select():
    def accept(sock):
        conn, addr = sock.accept()
        print('Connected by', addr)
        return conn

    def read(sock):
        data = sock.recv(1024)
        print('Received:', data)
        return data

    def write(sock, data):
        sock.send(data)
        print('Send:', data)

    def close(sock):
        sock.close()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8080))
    server.listen(5)
    server.setblocking(False)
    inputs = [server]
    outputs = []
    while True:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)
        for s in readable:
            if s is server:
                conn = accept(s)
                inputs.append(conn)
            else:
                data = read(s)
