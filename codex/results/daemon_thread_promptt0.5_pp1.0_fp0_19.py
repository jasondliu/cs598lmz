import threading
# Test threading daemon
def func1():
    while True:
        print("func1")
        time.sleep(1)
def func2():
    while True:
        print("func2")
        time.sleep(1)
t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)
t1.setDaemon(True)
t2.setDaemon(True)
t1.start()
t2.start()
t1.join()
t2.join()
