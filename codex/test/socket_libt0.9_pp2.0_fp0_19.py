import socket
import io

location = "/sys/class/gpio/gpio%s/value"

class LightBoardApp(object):
    def __init__(self, addr="0.0.0.0", port=42000):
        self.addr = addr
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.addr, self.port))
        # Create the connection
        self.data = {"conn": None, "data": None}
        
    def _connection(self):
        # Set to listen
        self.server.listen(5)
        # Accept new connections
        conn, addr = self.server.accept()
        # Set the property
        self.data['conn'] = conn
        # Set the data
        self.data['data'] = conn.makefile('r', 0)
        
