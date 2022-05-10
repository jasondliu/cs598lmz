import threading
# Test threading daemon
def worker():
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)
    t.join()

print('Exiting Main Thread')

# Test threading lock
import threading

class Counter(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increment(self):
        self.lock.acquire()
        self.value = value = self.value + 1
        self.lock.release()
        return value

counter = Counter()

class Worker(threading.Thread):
    def run(self):
        for i in range(10):
            value = counter.increment()
            print(value)

for i in range(2):
    Worker().start()

# Test threading condition
import threading
import time

class PeriodicTimer:
    def __init__(self, interval):
        self._interval
