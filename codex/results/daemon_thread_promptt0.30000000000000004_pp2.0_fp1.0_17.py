import threading
# Test threading daemon
def daemon():
    print('Start daemon')
    time.sleep(2)
    print('Exit daemon')

def non_daemon():
    print('Start non_daemon')
    print('Exit non_daemon')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non_daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

print('Exit main')

# Test threading lock
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

def worker():
    print('Worker', counter.increment())

threads = []
for i in range(2):
    t =
