import threading
# Test threading daemon
def func():
    print("func")
    time.sleep(2)
    print("func end")

t = threading.Thread(target=func)
t.setDaemon(True)
t.start()
print("main")

# Test threading lock
lock = threading.Lock()

def func1():
    lock.acquire()
    print("func1")
    time.sleep(2)
    print("func1 end")
    lock.release()

def func2():
    lock.acquire()
    print("func2")
    time.sleep(2)
    print("func2 end")
    lock.release()

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)
t1.start()
t2.start()

# Test threading RLock
lock = threading.RLock()

def func1():
    lock.acquire()
    print("func1")
    time.sleep(2)
    print("func1 end")
    lock.release()
