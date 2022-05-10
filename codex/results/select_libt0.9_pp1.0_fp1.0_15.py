import select
import sys
import threading
from threading import Thread


host_name = '145.24.222.121'
host_port = 6000
exitFlag = 0

class myThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global exitFlag
        print 'ex1'
        client()

    def stop(self):
        print 'ex3'
        exitFlag = 1
        self.is_alive()
        self._Thread__stop()

# create the server, binding the host address and port (tuple unwraps automatically)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host_name, host_port))
server.listen(5) # backlog of 5 unaccepted connections

conn = None

# accept incoming connections
conn, addr = server.accept()

BUFFER_SIZE = 2048
OBJECT_NAME = ''
s = socket.socket(socket.AF_INET, socket.
