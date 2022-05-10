import threading
# Test threading daemon
def test():
    while True:
        print("hello")
        time.sleep(1)

thread = threading.Thread(target=test,daemon=True)
thread.start()

print("main thread")
time.sleep(5)
print("main thread end")

# Test threading lock
lock = threading.Lock()
def test2():
    lock.acquire()
    print("hello")
    time.sleep(1)
    lock.release()

thread = threading.Thread(target=test2)
thread.start()

print("main thread")
time.sleep(5)
print("main thread end")

# Test threading event
event = threading.Event()
def test3():
    event.wait()
    print("hello")

thread = threading.Thread(target=test3)
thread.start()

print("main thread")
time.sleep(5)
event.set()
print("main thread end")

# Test threading condition
condition = threading.Condition()
def test4():
    condition.ac
