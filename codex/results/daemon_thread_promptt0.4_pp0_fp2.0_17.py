import threading
# Test threading daemon

def worker():
    print("worker")
    time.sleep(1)
    print("worker")

t = threading.Thread(target=worker)
t.setDaemon(True)
t.start()

print("main thread")

# Test threading join

def worker():
    print("worker")
    time.sleep(1)
    print("worker")

t = threading.Thread(target=worker)
t.start()
t.join()

print("main thread")

# Test threading lock

def worker():
    print("worker")
    time.sleep(1)
    print("worker")

t = threading.Thread(target=worker)
t.start()
t.join()

print("main thread")

# Test threading rlock

def worker():
    print("worker")
    time.sleep(1)
    print("worker")

t = threading.Thread(target=worker)
t.start()
t.join()

print("main thread")

# Test threading semaphore

