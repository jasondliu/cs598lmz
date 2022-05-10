import select

PORT = 8091
HOST = "127.0.0.1"

class Client:
        def __init__(self,host,port):
                self.host = HOST
                self.port = PORT
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
