import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()

# 一个简单的线程池
import threading, time
def worker(n):
    print('worker', n)
    time.sleep(1)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# 创建一个线程池，然后把任务放到线程池中，线程池会自动分配线程去执行任务
import concurrent.futures
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    for i in range(5):
        executor.submit(worker, i)


