import threading
# Test threading daemon
def worker():
    print("worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

print("Exiting Main Thread")

# Test threading lock
class Counter(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increment(self):
        self.lock.acquire()
        self.value = self.value + 1
        self.lock.release()

def worker(c):
    for i in range(10):
        c.increment()
    print("Value: ", c.value)

counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

print("Exiting Main Thread")

# Test threading condition
class Counter(object):
    def __init__(self):
       
