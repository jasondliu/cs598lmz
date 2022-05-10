import threading
threading.current_thread()

# creating own thread
import threading
from threading import Thread
class Adder(Thread):
    def __init__(self, items):
        self.items = items
        Thread.__init__(self)

    def run(self):
        total = 0
        for i in self.items:
            total += i
        print("Sum = " + str(total))
items = []
for i in range(0, 1000):
    items.append(i)
thread1 = Adder(items)
thread1.start()

# Synchronizing
import threading
from threading import Thread
class MyThread(Thread):
    def __init__(self, count, threadLock):
        self.count = count
        self.threadLock = threadLock
        Thread.__init__(self)

    def run(self):
        while self.count > 0:
            self.threadLock.acquire()
            print("Count value: " + str(self.count))
            self.count -= 1
            self.threadLock.release()
threadLock =
