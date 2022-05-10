import weakref

"""
This is a simple proxy to the QThread object.

It does not support the signals/slots mechanism of QThread,
but it does provide a simple interface for starting/stopping
the thread and checking if it is currently running.
"""
class Thread(QThread):
    def __init__(self, target, *args, **kwargs):
        super(Thread, self).__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.running = False
        self.finished = False

    def run(self):
        self.running = True
        self.finished = False
        self.target(*self.args, **self.kwargs)
        self.running = False
        self.finished = True

    def stop(self):
        self.terminate()
        self.wait()


