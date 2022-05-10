import threading
# Test threading daemon

def worker():
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print('Done')

# Test threading non-daemon
def worker():
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print('Done')

# Test threading non-daemon
def worker():
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print('Done')

# Test threading non-daemon
def worker
