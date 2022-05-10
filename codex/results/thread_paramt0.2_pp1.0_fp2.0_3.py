import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100)))))

# 实现一个简单的线程池
import queue
from threading import Thread

# 创建一个工作线程
def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()

# 创建线程池
q = queue.Queue()
for i in range(num_worker_threads):
    t = Thread(target=worker)
    t.daemon = True
    t.start()

# 提交工作请求
for item in source():
    q.put(item)

# 等待所有的工作完成
q.join()

# 创建一个线程池，并
