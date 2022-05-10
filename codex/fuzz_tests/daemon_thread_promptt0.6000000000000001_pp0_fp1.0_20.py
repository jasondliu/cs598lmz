import threading
# Test threading daemon
import time

class Timer(threading.Thread):
    def __init__(self, interval, function, args=[], kwargs={}):
        threading.Thread.__init__(self)
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.finished = threading.Event()

    def cancel(self):
        """Stop the timer if it hasn't finished yet."""
        self.finished.set()

    def run(self):
        while True:
            if self.finished.is_set(): return
            self.finished.wait(self.interval)
            if not self.finished.is_set():
                self.function(*self.args, **self.kwargs)

def function(arg1, arg2):
    print arg1, arg2

if __name__ == '__main__':
    timer = Timer(5.0, function, args=["hello", "world"])
    timer.start()
