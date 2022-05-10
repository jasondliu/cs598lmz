import threading
# Test threading daemon
def func1():
    while True:
        print("func1")
        time.sleep(3)

def func2():
    while True:
        print("func2")
        time.sleep(3)

t = threading.Thread(target=func1)
t.setDaemon(True)
t.start()

t2 = threading.Thread(target=func2)
t2.start()

t2.join()

print("end")
