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

# Test threading locks

lock = threading.Lock()

def worker():
    with lock:
        print("Worker")

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print("Exiting Main Thread")

# Test threading semaphore

semaphore = threading.Semaphore(0)

def worker():
    print("Worker")
    semaphore.release()

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(
