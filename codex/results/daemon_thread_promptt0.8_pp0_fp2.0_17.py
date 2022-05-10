import threading
# Test threading daemon
class threading_daemon(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        # The queue for store the data.
        self.queue = queue.Queue(20)
        self.timeout = 0.01
        self.debug = False
        self.stop = False
        self.thread = None
        self.thread_name = 'Base threading_daemon'
        self.callback = None

    # The set queue
    def setQueue(self, queue):
        self.queue = queue

    # The set timeout number
    def setTimeout(self, timeout):
        self.timeout = timeout

    # The set debug
    def setDebug(self, debug):
        self.debug = debug

    # The set thread name
    def setThreadName(self, thread_name):
        self.thread_name = thread_name

    # The set callback
    def setCallback(self, callback):
        self.callback = callback

    # The set stop
    def setStop(
