import threading
# Test threading daemon
# https://docs.python.org/2/library/multiprocessing.html#multiprocessing.Process
print "Test threading and daemon..."
global last_recv_time_tmp
global udp_socket
lock = threading.Lock()
udp_socket = None
last_recv_time_tmp = datetime.now()

class UDP_LISTENER(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, threadId, ip, port):
        super(UDP_LISTENER, self).__init__()
        self.threadId = threadId
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        self.udp_socket.bind((self.ip, self.port))
        self.stop_event = threading
