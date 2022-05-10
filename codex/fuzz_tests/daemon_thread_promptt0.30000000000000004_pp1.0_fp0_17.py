import threading
# Test threading daemon
def thread_test():
    while True:
        print("threading test")
        time.sleep(1)

t = threading.Thread(target=thread_test)
t.setDaemon(True)
t.start()

# Test threading lock
lock = threading.Lock()
def thread_test2():
    while True:
        lock.acquire()
        print("threading test2")
        lock.release()
        time.sleep(1)

t2 = threading.Thread(target=thread_test2)
t2.setDaemon(True)
t2.start()

# Test threading event
event = threading.Event()
def thread_test3():
    while True:
        event.wait()
        print("threading test3")
        time.sleep(1)

t3 = threading.Thread(target=thread_test3)
t3.setDaemon(True)
t3.start()

# Test threading condition
condition = threading.Condition()
def thread_test4():
    while True:
