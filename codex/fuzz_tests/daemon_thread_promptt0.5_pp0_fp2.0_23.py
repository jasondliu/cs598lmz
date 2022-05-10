import threading
# Test threading daemon
import time

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

print('Exiting main thread')

##
# Test threading daemon

def worker():
    print('Worker')
    time.sleep(2)
    print('Exiting worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print('Exiting main thread')
