import threading
threading.stack_size(67108864)

class Connection(threading.Thread):

    def __init__(self, socket, addr):
        threading.Thread.__init__(self)
        self.socket = socket
        self.addr = addr

    def run(self):
        print('Connection from: ' + str(self.addr))
        self.socket.send('Hello, client!'.encode('utf-8'))
        self.socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 8080))
server.listen(5)

while True:
    client_socket, addr = server.accept()
    Connection(client_socket, addr).start()
