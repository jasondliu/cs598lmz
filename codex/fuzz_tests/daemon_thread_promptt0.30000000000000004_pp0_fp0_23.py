import threading
# Test threading daemon
def worker(num):
    print('Worker: %s' % num)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Test threading join
def worker(num):
    """thread worker function"""
    print('Worker: %s' % num)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

# Test threading lock
def worker(num):
    """thread worker function"""
    print('Worker: %s' % num)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.
