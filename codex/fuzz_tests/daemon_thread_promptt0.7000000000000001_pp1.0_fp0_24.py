import threading
# Test threading daemon mode
def test(x):
    print(x)
    time.sleep(1)

for x in range(5):
    t = threading.Thread(target=test, args=(x,))
    t.setDaemon(True)
    t.start()
print("Main thread exit!")

# Test threading lock mode
lock = threading.RLock()
def test1():
    lock.acquire()
    print("hello world")
    time.sleep(2)
    lock.release()

for x in range(5):
    t = threading.Thread(target=test1)
    t.start()
print("Main thread exit!")
