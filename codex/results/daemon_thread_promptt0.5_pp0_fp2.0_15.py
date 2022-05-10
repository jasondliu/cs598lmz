import threading
# Test threading daemon
class Worker(threading.Thread):
    def __init__(self, name):
        super(Worker, self).__init__()
        self.name = name
        self.daemon = True
    def run(self):
        while True:
            print(self.name)
            time.sleep(1)

w = Worker('worker')
w.start()
time.sleep(3)
print('end')

# Test threading lock
lock = threading.Lock()
lock.acquire()
lock.acquire()

# Test threading RLock
lock = threading.RLock()
lock.acquire()
lock.acquire()

# Test threading Semaphore
sema = threading.Semaphore(5)
sema.acquire()
sema.release()

# Test threading Condition
cond = threading.Condition()
cond.wait()
cond.notify()

# Test threading Event
event = threading.Event()
event.wait()
event.set()

# Test threading Barrier
barrier = threading
