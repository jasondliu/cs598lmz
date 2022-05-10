import socket

def recvall(sock, n):
    data = ''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

def recv_all_json(sock):
    lengthbuf = recvall(sock, 4)
    length, = struct.unpack('!I', lengthbuf)
    data = recvall(sock, length)
    return json.loads(data)

def send_json(sock, data):
    data = json.dumps(data)
    length = struct.pack('!I', len(data))
    sock.sendall(length)
    sock.sendall(data)

def client(host, port):
    sock = socket.create_connection((host, port))
    data = {
        'ts': time.time(),
        'tal': [1,2,3],
    }
    send_json(sock, data)
