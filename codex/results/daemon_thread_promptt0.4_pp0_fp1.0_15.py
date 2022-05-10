import threading
# Test threading daemon

def worker():
    print("Worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

print("Main thread")

for t in threads:
    t.join()

print("All threads done")

# Test threading daemon

def worker():
    print("Worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()
    threads.append(t)

print("Main thread")

for t in threads:
    t.join()

print("All threads done")

# Test threading daemon

def worker():
    print("Worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()
    threads.append(
