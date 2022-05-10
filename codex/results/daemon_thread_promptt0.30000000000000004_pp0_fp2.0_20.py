import threading
# Test threading daemon

def worker():
    print("worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print("Exiting Main Thread")

# Test threading non-daemon

def worker():
    print("worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.setDaemon(False)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print("Exiting Main Thread")

# Test threading non-daemon

def worker():
    print("worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()
    threads.append(t)

for thread in threads:
