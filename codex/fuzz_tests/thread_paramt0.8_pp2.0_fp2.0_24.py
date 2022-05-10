import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x07')).start()

# 下面的代码输出结果将是什么？
import sys, threading

def fn(n):
    print('thread-{} started.'.format(n))
    return

threads = []
for i in range(5) :
    t = threading.Thread(target=fn, args=(i, ))
    threads.append(t)
    t.start()

for i, t in enumerate(threads) :
    print('thread-{} joined.'.format(i))
    t.join()

# 下面的代码输出结果将是什么？
import threading, time

def execute(n):
    print('Thread {} started.'.format(n))
    time.sleep(3)
    print('Thread {} finished.'.format(n))

threads = []
for i in range(5
