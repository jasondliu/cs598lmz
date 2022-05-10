import threading
# Test threading daemon
class ThreadClass(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + ' @ ' + str(i)
            print(msg)

for i in range(5):
    t = ThreadClass()
    t.start()

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

def run_threads(func, c):
    threads = []
    for i in range(5):
        t = threading.Thread(target=func, args=(c,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

c =
