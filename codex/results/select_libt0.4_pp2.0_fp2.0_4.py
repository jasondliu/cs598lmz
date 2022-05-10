import select

class Server:
    def __init__(self, port):
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("0.0.0.0", port))
        self.server_socket.listen()
        self.clients = {}
        self.fileno_to_socket = {self.server_socket.fileno(): self.server_socket}

    def run(self):
        while True:
            rlist, wlist, xlist = select.select(self.fileno_to_socket.keys(), [], [])
            for ready_socket in rlist:
                if ready_socket == self.server_socket.fileno():
                    new_socket, addr = self.server_socket.accept()
                    self.clients[new_socket.fileno()] = addr
                    self.fil
