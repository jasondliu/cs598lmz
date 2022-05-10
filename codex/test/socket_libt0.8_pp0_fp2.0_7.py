import socket
import pickle

from bitstring import ConstBitStream


class Client:

    def __init__(self, host='20.42.77.116', port=5555):
        self.host = host
        self.port = port
        self.server_address = (self.host, self.port)

        self.connection = None

        self.create_connection()

    def create_connection(self, tries=0):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect(self.server_address)

    def send_message(self, msg):
        try:
            self.connection.sendall(pickle.dumps(msg))
        except ConnectionResetError:
            self.create_connection()
            self.send_message(msg)
        except AttributeError:
            print('Connection is broken')
            self.create_connection()

