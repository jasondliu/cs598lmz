import select
# Test select.select
print('Select.select test')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 0))
sock.listen(5)
port = sock.getsockname()[1]
print('port: %s' % port)

def echo_server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        while True:
            data = conn.recv(1024)
            if len(data) == 0: break
            conn.send(data)
        conn.close()

def echo_client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', port))
    for i in range(10):
        sock.send(b'%d\r\n' % i)
        print
