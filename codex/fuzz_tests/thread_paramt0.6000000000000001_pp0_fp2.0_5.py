import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello world"), daemon=True).start()

# 11.7.1.2. 创建线程的第二种方法
import threading
class MyThread(threading.Thread):
    def run(self):
        print('hello world')

t = MyThread()
t.start()

# 11.7.1.3. 使用线程池
import concurrent.futures
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(lambda: sys.stdout.write("hello world\n"))
    executor.submit(lambda: sys.stdout.write("hello again\n"))

# 11.7.2. 启动大量的线程
# 11.7.2.1. 创建大量的线程
import threading
threads = []
for _ in range(10):

