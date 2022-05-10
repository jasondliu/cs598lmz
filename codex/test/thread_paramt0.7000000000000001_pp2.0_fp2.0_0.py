import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
time.sleep(0.5)

print('\n'*2)
#The Queue class in this module implements all the required locking semantics.
import Queue
import threading

class Worker(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue
    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            directory, filenames = self._queue.get()
            for filename in filenames:
                self._process(directory, filename)
            self._queue.task_done()
    def _process(self, directory, filename):
        print('%s: %s' % (self.name, os.path.join(directory, filename)))

class ThreadPool:
    def __init__(self, num_threads):
        self._queue = Queue.Queue()
