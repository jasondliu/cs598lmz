import socket

class Client:
    def __init__(self, port, host = '', filename = ''):
        self.port = port
        self.host = host
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host,port))
        self.file_name = filename
    def RecvFile(self):
        fp = open(self.file_name, 'wb')
        data = self.sock.recv(4)
        try:
            file_size = struct.unpack('!I', data)[0]
        except struct.error:
            print('struct error')
        recvd_size = 0
        while not recvd_size == file_size:
            if file_size - recvd_size > 1024:
                size = 1024
            else:
                size = file_size - recvd_size
            data = self.sock.recv(size)
            recvd_size += len(data)
            fp.write(data)
        else:
