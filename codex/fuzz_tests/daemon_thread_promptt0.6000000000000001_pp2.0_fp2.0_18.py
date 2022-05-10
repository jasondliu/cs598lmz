import threading
# Test threading daemon to send messages in the background
class ThreadingDaemon(threading.Thread):
    def __init__(self, function, *args, **kwargs):
        threading.Thread.__init__(self)
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.setDaemon(True)
        self.start()

    def run(self):
        self.function(*self.args, **self.kwargs)
