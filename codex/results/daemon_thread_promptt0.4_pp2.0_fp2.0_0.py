import threading
# Test threading daemon
import time

class MyDaemon(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num
    def run(self):
        print("I am thread %d" % self.num)
        time.sleep(1)

for i in range(10):
    t = MyDaemon(i)
    t.setDaemon(True)
    t.start()

print("Main thread is finished")
