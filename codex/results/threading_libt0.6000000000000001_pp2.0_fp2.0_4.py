import threading
threading.stack_size(67108864)

class Server(object):
    def __init__(self):
        self.ip = ""
        self.port = 0
        self.thread_count = 0
        self.threads = []

    def start(self, ip, port, thread_count):
        self.ip = ip
        self.port = port
        self.thread_count = thread_count
        for i in range(self.thread_count):
            self.threads.append(ProxyThread(self.ip, self.port))
        for t in self.threads:
            t.start()
        for t in self.threads:
            t.join()


class ProxyThread(threading.Thread):
    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_
