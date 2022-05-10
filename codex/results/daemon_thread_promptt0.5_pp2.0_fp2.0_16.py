import threading
# Test threading daemon
def daemon():
    print("Start daemon")
    x = 0
    while True:
        time.sleep(1)
        print("Daemon %i" % x)
        x += 1
    print("End daemon")

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

print("Start main thread")
d.start()
time.sleep(3)
print("End main thread")

# Test threading lock
class Counter(object):
    def __init__(self, start = 0):
        self.lock = threading.Lock()
        self.value = start
    def increment(self):
        self.lock.acquire()
        self.value += 1
        self.lock.release()

def worker(c):
    for i in range(2):
        c.increment()
    print("Done")

counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

print("Waiting
