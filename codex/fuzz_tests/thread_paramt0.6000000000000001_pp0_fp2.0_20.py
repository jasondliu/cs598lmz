import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# 4.2.2 启动一个线程并等待它结束
import time
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()

# 4.2.3 判断线程是否已经启动
t.is_alive()

# 4.2.4 用线程执行多个任务
def worker(n):
    for i in range(n):
        time.sleep(1)
        print(threading.current_thread().name, i)

for
