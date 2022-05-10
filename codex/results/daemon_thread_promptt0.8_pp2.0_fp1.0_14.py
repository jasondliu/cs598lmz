import threading
# Test threading daemon

class TestThread(threading.Thread):
    def run(self):
        for i in range(3):
            print("Thread Name: {}\tThread ID: {}\tIteration: {}".format(self.name, self.ident, i))
            time.sleep(random.randint(1, 3))
        print("Thread Name: {}\tThread ID: {}\tCompleted".format(self.name, self.ident))

print("Main thread started")

for i in range(5):
    TestThread().start()

print("Main thread ended")
 

# Using threading with return

from threading import Thread
from queue import Queue

def worker(q,n):
    for i in range(n):
        item = q.get()
        print("Thread {} got {}".format(n,item))
        q.task_done()

q = Queue()

for x in range(5):
    t = Thread(target=worker, kwargs={'q': q, 'n': x})
    t.start()
    

