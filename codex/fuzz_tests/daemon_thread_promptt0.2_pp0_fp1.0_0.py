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

# Test threading daemon

import threading
import time

def worker():
    print('Worker')
    time.sleep(1)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print('Exiting')

# Test threading daemon

import threading
import time

def worker():
    print('Worker')
    time.sleep(1)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()
   
