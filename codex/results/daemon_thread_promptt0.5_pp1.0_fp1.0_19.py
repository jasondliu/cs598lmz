import threading
# Test threading daemon

def run_thread(n):
    print('thread {} started'.format(n))
    time.sleep(1)
    print('thread {} ended'.format(n))

for i in range(5):
    t = threading.Thread(target=run_thread, args=(i,))
    t.setDaemon(True)
    t.start()

print('main thread ended')

# Test threading Lock
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

def worker(id):
    for i in range(10):
        value = counter.increment()
        print('worker {} got value {}'.format(id, value))

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(
