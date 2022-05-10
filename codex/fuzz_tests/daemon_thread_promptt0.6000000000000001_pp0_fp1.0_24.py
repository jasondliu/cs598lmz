import threading
# Test threading daemon
def run():
    time.sleep(2)
    print("threading daemon run")
t = threading.Thread(target=run, daemon=True)
t.start()
print("main thread")

# Test threading join
def run2():
    time.sleep(2)
    print("threading join run")
t2 = threading.Thread(target=run2)
t2.start()
t2.join()
print("main thread")


# Test threading Lock
lock = threading.Lock()
def run3():
    with lock:
        print("threading lock run")

t3 = threading.Thread(target=run3)
t4 = threading.Thread(target=run3)
t3.start()
t4.start()
t3.join()
t4.join()
print("main thread")

# Test threading Semaphore
sm = threading.Semaphore(2)
def run4():
    with sm:
        print("threading semaphore run")

t5 = threading.Thread(target=
