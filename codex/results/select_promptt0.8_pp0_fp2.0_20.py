import select
# Test select.select
from socket import *

def get_ports(sock_type=SOCK_STREAM, port=10000, num=10):
    ports = []
    while len(ports) < num:
        try:
            s = socket(AF_INET, sock_type)
            s.bind(('', port))
        except OSError:
            port += 1
        else:
            ports.append(port)
            port += 1
            s.close()
    return ports

def server():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', 10000))
    sock.listen(5)
    while True:
        sc, addr = sock.accept()
        print('Got connection from', addr)
        msg = sc.recv(1024)
        print(msg)
        sc.send(b'Echo => ' + msg)
        sc.close()

def client(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost', port))

