import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stopFlag = threading.Event()
        self.setDaemon(True)
        self.start()

    def run(self):
        while not self.stopFlag.isSet():
            print("hello")
            self.stopFlag.wait(1)

    def stop(self):
        self.stopFlag.set()

t = MyThread()
t.stop()

# Test threading queue
import queue
import threading

q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())
print(q.empty())

q.put(4)
print(q.get())

# Test threading locks
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, id, lock):
        threading.Thread.
