import socket
import sys

class Client:


    def __init__(self, ip, port, timeout=None):
        self.ip = ip
        self.port = port
        self.timeout = timeout if timeout is not None else 5


    def get(self, metric):
        with socket.create_connection((self.ip, self.port), self.timeout) as sock:
            try:
                request = f'get {metric}\n'.encode()
                sock.sendall(request)
                data = []
                while True:
                    packet = sock.recv(1024)
                    data.append(packet)
                    if not packet or packet.decode().endswith('\n\n'):
                        break
                response = b''.join(data).decode()
                return [tuple(line.split(' ')) for line in response.strip().split('\n')]
            except Exception as e:
                raise ClientError


    def put(self, metric, value, timestamp=None):
        timestamp = timestamp or int(time.time())
