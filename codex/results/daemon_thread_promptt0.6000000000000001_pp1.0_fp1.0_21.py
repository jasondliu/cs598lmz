import threading
# Test threading daemon
def run(x):
    while True:
        print(x)
        time.sleep(1)

t = threading.Thread(target=run, args=(6,))
t.daemon = True
t.start()

while True:
    print("Main")
    time.sleep(1)

# Test threading in queue
from queue import Queue
import threading

def run(x):
    while True:
        x.get()
        print("Thread")
        time.sleep(1)

q = Queue()
t = threading.Thread(target=run, args=(q,))
t.daemon = True
t.start()

while True:
    q.put(1)
    print("Main")
    time.sleep(1)

# Test threading in queue
from queue import Queue
import threading

def run(q):
    while True:
        q.get()
        print("Thread")
        time.sleep(1)

q = Queue()
t = threading.Thread(target=run,
