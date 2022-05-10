import threading
# Test threading daemon
def runInThread(fn):
    def run(*k, **kw):
        t = threading.Thread(target=fn, args=k, kwargs=kw)
        t.setDaemon(True)
        t.start()
    return run

class Player(Player):
    def __init__(self, sock, addr, name):
        Player.__init__(self, sock, addr, name)
        self.gui = None
        self.game = None

    @runInThread
    def recvMessage(self):
        while True:
            data = self.sock.recv(1024).decode('utf-8')
            print('Received message: ', data)
            message = data.split(' ')
            if message[0] == 'login':
                self.name = message[1]
                self.sock.sendall(('login success').encode('utf-8'))
                self.gui.playerLogin(self)
            elif message[0] == 'ready':
                self.gui.readyToPlay(self)
            el
