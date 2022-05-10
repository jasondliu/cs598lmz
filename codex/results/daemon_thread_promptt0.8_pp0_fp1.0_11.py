import threading
# Test threading daemon
def test_daemon():
    print("Start")
    time.sleep(0.2)
    print("End")

thread = threading.Thread(target=test_daemon, daemon=True)
print("Main: start")
thread.start()
print("Main: end")

# Test threading event
def waiter(e):
    print("wait for event")
    e.wait() # block until the event is set
    print("got event")

e = threading.Event()
w = threading.Thread(target=waiter, args=(e,))
w.start()

e.set() # set event, then waiter() can be continue

# Test threading lock
def worker(n, lock):
    lock.acquire()
    print("hello", n)
    lock.release()

lock = threading.Lock()
for n in range(3):
    t = threading.Thread(target=worker, args=(n,lock))
    t.start()
print("Main: end")


# Threading barrier
print("Main: start")

