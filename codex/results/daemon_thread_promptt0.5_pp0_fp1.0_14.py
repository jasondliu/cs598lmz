import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        while True:
            print("Hello")
            time.sleep(1)

thread = MyThread()
thread.start()

print("Main thread")
time.sleep(5)
print("Main thread again")
time.sleep(5)

print("Done")

# Test threading queue

from queue import Queue

class MyThread(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.daemon = True
        self.q = q

    def run(self):
        while True:
            if self.q.qsize() > 0:
                print(self.q.get())
            time.sleep(1)

q = Queue()
thread = MyThread(q)
thread.start()

print("Main thread")
q.put("Hello")
time
