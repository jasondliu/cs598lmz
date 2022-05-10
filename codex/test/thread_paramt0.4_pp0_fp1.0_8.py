import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello World\n')).start()

# 在线程中执行线程
import threading
def action(max):
    for i in range(max):
        print(threading.current_thread().name + " " + str(i))

threading.Thread(target=action, args=(100,), name="新线程").start()

# 创建线程类
import threading
class MyThread(threading.Thread):
    def __init__(self, name, user):
        threading.Thread.__init__(self)
        self.t_name = name
        self.user = user
    def run(self):
        print("Hello " + self.user + " from " + self.t_name)

t = MyThread("Thread-1", "Hacker")
t.start()

# 线程同步
import threading
import time
