import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread2\n'), name='Thread2').start()
threading.Thread(target=lambda: sys.stdout.write('Thread1\n'), name='Thread1').start()

# threading: Queue
from queue import Queue
from threading import Thread

def worker(q):
    while True:
        item = q.get()
        print('Got:', item)
        q.task_done()

q = Queue()
for i in range(10):
    t = Thread(target=worker, args=(q,))
    t.daemon = True
    t.start()

for item in range(50):
    q.put(item)

q.join()

# threading: Semaphore
from threading import Thread
import urllib.request
from queue import Queue
import time
from threading import Semaphore

class Downloader(Thread):
    def __init__(self, url_queue, semaphore):
        super().__init__()
        self.url_queue = url_queue
