import threading
# Test threading daemon
def test():
    while True:
        print("test")
        time.sleep(1)

t = threading.Thread(target=test)
t.setDaemon(True)
t.start()

# Test threading lock
lock = threading.Lock()
def test2():
    lock.acquire()
    print("test2")
    lock.release()

t2 = threading.Thread(target=test2)
t2.start()

# Test threading event
event = threading.Event()
def test3():
    event.wait()
    print("test3")

t3 = threading.Thread(target=test3)
t3.start()

# Test threading semaphore
semaphore = threading.Semaphore(3)
def test4():
    semaphore.acquire()
    print("test4")
    semaphore.release()

t4 = threading.Thread(target=test4)
t4.start()

# Test threading condition
condition = threading.Condition()
def test
