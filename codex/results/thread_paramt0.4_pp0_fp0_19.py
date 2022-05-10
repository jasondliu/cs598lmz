import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('thread2\n')).start()

# thread1
# thread2

# 主线程会等待所有线程退出后再退出

# 实现多线程的第二种方式是通过继承Thread类
# 实现一个Thread类，继承Thread类，并重写run方法
import sys, threading
class MyThread(threading.Thread):
    def run(self):
        sys.stdout.write('thread\n')

thread = MyThread()
thread.start()

# thread

# 如果要实现多线程，那
