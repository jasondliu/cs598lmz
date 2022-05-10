import threading
# Test threading daemon
import time

def worker():
    print("worker")
    time.sleep(1)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

print("threads:",threads)

# Test threading lock
import threading
import time

class Box(object):
    lock = threading.RLock()
    def __init__(self):
        self.total_items = 0

    def execute(self, n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()

    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()

    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()

def adder(box, items):
    while items > 0:
        print("adding 1 item in the box")
        box
