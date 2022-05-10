import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Beautiful\n')).start()
threading.Thread(target=lambda: sys.stdout.write('World\n')).start()

# 使用threading模块创建线程
# 方法一：将要执行的方法作为参数传给Thread的构造方法
import threading, time
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)
print('thread %s is running...' % threading.current_thread().name)

