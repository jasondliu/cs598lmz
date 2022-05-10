import threading
# Test threading daemon mode
#

# Define a reader thread for testing
class ReaderThread(threading.Thread):
    def __init__(self, parent, socket):
        threading.Thread.__init__(self)
        self.parent = parent
        self.socket = socket
        self.buffer = ''
        self.msg = ''
        self.running = True
        
    def run(self):
        while self.running:
            char = self.socket.recv(1)
            if char != '\n':
                self.buffer += char
            else:
                self.msg = self.buffer
                self.buffer = ''
                log.debug(self.msg)

    def stop(self):
        if not self.running:
            return
        self.running = False
        self.join()

    def readln(self):
        #log.debug('ReaderThread.readln()')
        buf = self.msg
        self.msg = ''
        return buf
        

# Define test class
class TestServer(unittest.TestCase):
    def setUp
