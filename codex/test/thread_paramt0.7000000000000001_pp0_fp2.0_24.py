import sys, threading
threading.Thread(target=lambda: sys.stdout.write("threading\n")).start()
# threading

# threading.enumerate() 返回正在运行的线程的list
# 只要调用start开始线程，线程就是active的
import time

def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(0)
    print(threading.currentThread().getName(), 'Exiting')

def my_service():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(0)
    print(threading.currentThread().getName(), 'Exiting')

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start
