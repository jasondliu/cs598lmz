import threading
threading.stack_size(8720 * 4096)

class Client(object):
    def __init__(self, host = 'localhost', port = 9123):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        self.name = ''

        self.s.sendall('login anonymous\n')
        self.s.sendall('protocol 4\n')
        self.s.sendall('ucinewgame\n')
        self.s.sendall('isready\n')
        self.s.sendall('stop\n')


    def __del__(self):
        self.s.close()

    def analyze(self, fen, depth):
        self.s.sendall('position fen ' + fen + '\n')
        self.s.sendall('go depth ' + str(depth) + '\n')
        ret = ''
        
        while True:
            data = self.s.recv(1024)

            if data.
