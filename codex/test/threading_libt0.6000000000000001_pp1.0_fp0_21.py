import threading
threading.Thread(target=f).start()

class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))
        time.sleep(1)
        print("{} finished!".format(self.getName()))

for x in range(4):
    mythread = MyThread(name = "Thread-{}".format(x + 1))
    mythread.start()
    time.sleep(1)

import queue

class MyThread(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q
    def run(self):
        while True:
            counter = self.q.get()
            print(counter)
            time.sleep(1)
            self.q.task_done()

q = queue.Queue()

for x in range(10):
    mythread = MyThread(q)
    mythread.setDaemon(True)
    mythread.start()

