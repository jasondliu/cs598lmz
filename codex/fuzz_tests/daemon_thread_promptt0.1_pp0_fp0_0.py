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

for thread in threads:
    thread.join()

print("Done")

# Test threading daemon

def worker():
    print("Worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print("Done")

# Test threading daemon

def worker():
    print("Worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print("Done")

