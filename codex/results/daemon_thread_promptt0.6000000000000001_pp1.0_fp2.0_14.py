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

for thread in threads:
    thread.join()

print('Exiting')

# Test threading
import threading

class MyClass(threading.Thread):
    def run(self):
        print('running')

for i in range(5):
    t = MyClass()
    t.start()

print('Exiting')
# Test threading lock
import threading

lock = threading.Lock()

print('First try :', lock.acquire())
print('Second try:', lock.acquire(0))

# Test threading lock
import threading

lock = threading.Lock()

print('First try :', lock.acquire())
print('Second try:', lock.acquire(0))
# Test threading
import threading

def worker(num):
    """thread worker function"""

