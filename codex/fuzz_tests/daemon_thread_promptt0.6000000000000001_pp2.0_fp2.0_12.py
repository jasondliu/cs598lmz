import threading
# Test threading daemon
def worker(num):
    print('Worker {0}'.format(num))
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

print('hello')

import time
import threading

def worker():
    print('Worker')
    time.sleep(1)
    return

print('hello')
threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

print('hello')
