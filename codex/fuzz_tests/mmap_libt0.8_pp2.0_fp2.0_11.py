import mmap

TELNET_PORT = 79
TELNET_TIMEOUT = 5

class TelnetServer(threading.Thread):
    def __init__(self):
        super(TelnetServer, self).__init__()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('0.0.0.0', TELNET_PORT))
        self.server.listen(1)
        self.object = None
        self.daemon = True

    def run(self):
        print 'server running'
        try:
            while True:
                client = self.server.accept()[0]
                client.settimeout(TELNET_TIMEOUT)
                print 'telnet connected'
                while True:
                    try:
                        data = client.recv(1024)
                        if data:
                            print 'received: %s' % data
                           
