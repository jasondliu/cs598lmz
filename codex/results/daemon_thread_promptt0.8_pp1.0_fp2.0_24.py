import threading
# Test threading daemon

def f(name):
    print('hello', name)

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=f, args=(i,))
        t.setDaemon(True) # 主线程结束，子线程也就自动结束了，不需要额外设置结束了。
        t.start()

 

# 线程优先级队列（ Queue）

import queue
import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self
