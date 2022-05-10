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
    t.daemon = True
    t.start()
    threads.append(t)

print("Exiting Main Thread")

# Test threading lock

lock = threading.Lock()

def worker_with(lock):
    with lock:
        print(threading.current_thread().getName(),'Start')
        time.sleep(2)
        print(threading.current_thread().getName(),'End')

def worker_no_with(lock):
    lock.acquire()
    print(threading.
