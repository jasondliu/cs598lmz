import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            print("hello, world")
            time.sleep(1)

if __name__ == '__main__':
    thread = MyThread()
    thread.setDaemon(True)
    thread.start()
    print("main thread starts")
    time.sleep(3)
    print("main thread ends")

# Test threading non-daemon
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            print("hello, world")
            time.sleep(1)

if __name__ == '__main__':
    thread = MyThread()
    thread.start()
    print("main thread starts")
    time.sleep(3)
    print("main thread ends")

# Test threading lock
import threading

class MyThread(
