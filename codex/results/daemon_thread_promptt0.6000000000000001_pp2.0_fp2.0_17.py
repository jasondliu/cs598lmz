import threading
# Test threading daemon
class ThreadingDaemon(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.stopFlag = threading.Event()
    def run(self):
        print "Starting " + self.name
        while not self.stopFlag.isSet():
            time.sleep(1)
        print "Exiting " + self.name
    def join(self, timeout=None):
        self.stopFlag.set()
        threading.Thread.join(self, timeout)

daemon = ThreadingDaemon("ThreadingDaemon")
daemon.setDaemon(True)
daemon.start()

# Test threading daemon
class ThreadingDaemon2(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.stopFlag = threading.Event()
    def run(self):
        print "Starting " + self.name
        while not self.stopFlag.
