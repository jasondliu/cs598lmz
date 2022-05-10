import select
# Test select.select()

def server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))
    s.listen(1)
    while True:
        client, addr = s.accept()
        print('Connection from', addr)
        client.sendall(b'Welcome to the server. Type "quit" to exit.\n')
        while True:
            data = client.recv(1024)
            if not data:
                break
            client.sendall(data)
            if data.rstrip() == b'quit':
                break
        client.close()
        print('Connection closed')

def client(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', port))
    while True:
        ready = select.select([s], [], [], 1)
