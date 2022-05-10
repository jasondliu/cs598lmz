import select
# Test select.select()

# Create a pair of connected sockets

# Create a pair of connected sockets

def child():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 16000))
    while True:
        msg = input('Enter message to send: ')
        sock.send(msg.encode('ascii'))
        data = sock.recv(1024)
        print('Received:', data.decode('ascii'))

def parent():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 16000))
    sock.listen(1)
    while True:
        conn, addr = sock.accept()
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            print('Received:', data.decode('ascii'))
            conn.send(data)
        conn.close()

if __
