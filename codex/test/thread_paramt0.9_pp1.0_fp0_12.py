import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread started\n')).start()

# 获取当前线程信息
# threading模块使用一个线性有界缓冲队列来保存活动线程，
# 每个线程都是队列的一项，队列开始填满以后，进一步创建的线程会被挂起（减速）
# threading.enumerate() 可以获取所有活动线程
import random, threading, time
def worker():
    pause = random.randint(1, 5) / 5
    time.sleep(pause)
