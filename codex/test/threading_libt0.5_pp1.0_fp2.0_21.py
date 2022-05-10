import threading
threading.stack_size(2**27)
import sys

class ThreadWithReturnValue(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return

def process(n):
    print("Processing {}".format(n))
    return n

if __name__ == "__main__":
    # Multithread
    results = []
    for i in range(5):
        print("Spawning {}".format(i))
