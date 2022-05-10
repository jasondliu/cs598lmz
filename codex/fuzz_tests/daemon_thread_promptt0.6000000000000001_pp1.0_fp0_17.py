import threading
# Test threading daemon
class Test(threading.Thread):
    def run(self):
        while True:
            print(self)
            time.sleep(1)

for i in range(3):
    t = Test()
    t.setDaemon(True)
    t.start()

for i in range(3):
    print(i)
    time.sleep(1)

print("done")

# Test threading lock
lock = threading.Lock()

class Test(threading.Thread):
    def run(self):
        if lock.acquire():
            print(self)
            time.sleep(1)
            lock.release()

for i in range(3):
    t = Test()
    t.start()

for i in range(3):
    print(i)
    time.sleep(1)

print("done")

lock = threading.RLock()
lock.acquire()
lock.acquire()
lock.release()
lock.release()

# Test threading event
e = threading.Event()

class Test
