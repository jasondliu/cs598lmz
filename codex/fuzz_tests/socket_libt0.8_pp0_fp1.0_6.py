import socket
import sys
import json

class Client():
    def __init__(self, server_address, port, filename):
        self.server_address = server_address
        self.port = port
        self.filename = filename
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def get_file(self):
        try:
            self.sock.connect((self.server_address, self.port))
            self.sock.sendall(self.filename.encode())

            # Begin receiving process of the file
            received = self.sock.recv(128)
            print("Confirmation: {}".format(received.decode()))
            chunk_size = 4096
            with open(self.filename, 'wb') as f:
                while True:
                    chunk = self.sock.recv(chunk_size)
                    if chunk:
                        f.write(chunk)
                        # self.sock.sendall(b'OK')
                    else:
                        self.sock.sendall(
