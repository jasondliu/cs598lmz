import threading
# Test threading daemonic process


def daemon():
    print("Starts\n")
    time.sleep(2)
    print("Exiting\n")


d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
d.start()
d.join(1)
# Test threading locks
lock = threading.Lock()
x = 0


def addition():
    global x
    lock.acquire()
    for i in range(100):
        x += 1
    lock.release()


def subtraction():
    global x
    lock.acquire()
    for i in range(100):
        x -= 1
    lock.release()


additionThread = threading.Thread(target=addition, args=(), name="addition")
subtractionThread = threading.Thread(target=subtraction, args=(), name="subtraction")

additionThread.start()
subtractionThread.start()

additionThread.join()
subtractionThread.join()

print(x)
# Test thread
