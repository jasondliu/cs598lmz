import sys, threading
threading.Thread(target=lambda: sys.stdout.write('hello world\n')).start()

# 创建一个线程实例，并传给它一个可调用的类实例
import threading
class Mythread(threading.Thread):
    def run(self):
        pass
for i in range(10):
    t = Mythread()
    t.start()

# 创建一个线程实例，并传给它一个可调用的实例
import threading
class Power:
    def __init__(self, i):
        self.i = i
    def action(self):
        # 打印i的平方
        print(self.i ** 2)
threads = []
for i in range(10):
    t = threading.Thread(target=Power(i).action)
