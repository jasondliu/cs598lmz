import threading
# Test threading daemon

def worker():
    print("I am worker")
    time.sleep(5)
    print("worker finished")

t = threading.Thread(target=worker)
t.setDaemon(True)
t.start()
print("main thread finished")

# Test threading lock
lock = threading.Lock()

def worker2(i):
    print("worker2 %d" % i)
    lock.acquire()
    print("worker2 %d" % i)
    lock.release()

for i in range(10):
    t = threading.Thread(target=worker2, args=(i,))
    t.start()

# Test threading semaphore
semaphore = threading.Semaphore(2)

def worker3(i):
    semaphore.acquire()
    print("worker3 %d" % i)
    time.sleep(3)
    print("worker3 %d" % i)
    semaphore.release()

for i in range(10):
    t = threading.Thread(target=
