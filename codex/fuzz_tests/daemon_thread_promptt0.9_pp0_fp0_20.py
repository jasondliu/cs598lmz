import threading
# Test threading daemon
class _MyThread(threading.Thread):
    def __init__(self, queue, callback):
        super(_MyThread, self).__init__()
        self.queue = queue
        self.callback = callback
        self.daemon = True
        self.start() # start the thread

    def stop(self):
        print(self.name + " stopped running")

    def run(self):
        print(self.name + " started running")

        while True:
            item = self.queue.get()
            self.callback(item)
            self.queue.task_done()
            print(self.name + " is running")

class Grapher(object):
    def __init__(self):
        self.multiplex = []
        self.graphs = []
        self.state_seq = []
        self.count = 0
        self.mutex = threading.Lock()
        self.is_busy = False
        #self.queue = queue.Queue(maxsize=5)
        self.queue = queue.Queue()
        self.thread =
