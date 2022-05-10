import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello world\n')).start()

#4.4
from time import sleep
from threading import Thread, Lock

class Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset

def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        # Read from seonsor
        counter.increment(1)

def run_threads(func, how_many, counter):
    threads = []
    for i in range(5):
        args = (i, how_many, counter)
        thread = Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

how_many = 10 ** 5
counter = Counter()
run_threads(worker, how_many, counter)
print('Counter should be {0}, found {1}'.format(5 * how_many, counter.count))
