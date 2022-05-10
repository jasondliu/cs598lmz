import select
import socket
import sys
import re

def write_log(text):
    sys.stdout.write("%s: %s\n" % (time.ctime(), text))
    sys.stdout.flush()
    
class FuncThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)
    def run(self):
        self._target(*self._args)

class ThreadPool(threading.Thread):
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.threads = []
        threading.Thread.__init__(self)

    def run(self):
        for i in range(self.num_threads):
            t = threading.Thread(target=self._thread_func)
            t.start()
            self.threads.append(t)
        for t in self.threads:
            t.join()


