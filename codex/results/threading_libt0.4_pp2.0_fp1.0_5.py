import threading
threading.currentThread().getName()

# 线程优先级队列（ Queue）
import queue
q = queue.Queue(maxsize=10)
for i in range(10):
    q.put(i)
while not q.empty():
    print(q.get())

# 线程同步
# Event对象
# 信号量 Semaphore
import threading, time
class Hider(threading.Thread):
    def __init__(self, cond, name):
        super().__init__()
        self.cond = cond
        self.name = name

    def run(self):
        time.sleep(1)
        self.cond.acquire()
        print(self.name + ': 我已经把眼睛蒙上了')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 我找
