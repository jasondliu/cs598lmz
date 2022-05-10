import threading
# Test threading daemon
# http://stackoverflow.com/questions/1408356/keyboard-interrupts-with-pythons-multiprocessing-pool

class InterruptableThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
        self._verbose = Verbose

    def run(self):
        if self._verbose:
            print('thread started...')
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
        if self._verbose:
            print('thread finished...')

    def join(self, timeout=None):
        threading.Thread.join(self)
        return self._return

def _worker(i):
    print('worker:', i)
    time.sleep(i)
    return i

def
