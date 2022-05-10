import threading
# Test threading daemon

def hello():
    while True:
        print('hello')
        time.sleep(1)

t = threading.Thread(target=hello)
t.setDaemon(True)
t.start()

time.sleep(5)
print('main thread')

# Test threading lock

def hello2():
    while True:
        lock.acquire()
        print('hello')
        time.sleep(1)
        lock.release()

lock = threading.Lock()
t2 = threading.Thread(target=hello2)
t2.setDaemon(True)
t2.start()

time.sleep(5)
print('main thread')

# Test threading RLock

def hello3():
    while True:
        lock.acquire()
        print('hello')
        time.sleep(1)
        lock.release()

lock = threading.RLock()
t3 = threading.Thread(target=hello3)
t3.setDaemon(True)
t3.start()

time.sleep(5
