import select
import sys

class ClientHandler:
    """
    Handles the client socket and reads the messages from the server.
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.nickname = None
        self.buffer = ''
        self.connection_active = False

    def connect(self, nickname):
        """
        Connects to the server
        :param nickname: The nickname of the client
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.socket.setblocking(0)
        self.nickname = nickname
        self.connection_active = True
        self.send_message(nickname)

    def send_message(self, message):
        """
        Sends a message to the server
        :param message: The message to be sent
        """
        self.socket.send(message.encode())

