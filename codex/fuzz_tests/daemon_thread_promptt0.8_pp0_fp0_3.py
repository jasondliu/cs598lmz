import threading
# Test threading daemon usage
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s: %(message)s'
)
import multiprocessing

class Counter:
    def __init__(self, start = 0):
        self.lock = threading.Lock()
        self.value = start
    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1
        finally:
            self.lock.release()

def worker(c):
    logging.debug('Starting')
    for i in range(2):
        pause = random.random()
        logging.debug('Sleeping %0.02f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Exiting')

counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))

