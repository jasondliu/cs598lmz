import threading
threading.stack_size(67108864)

p1 = multiprocessing.Process(target=func1)
p2 = multiprocessing.Process(target=func2)
p1.start()
p2.start()
p1.join()
p2.join()
</code>
This works. But I prefer to use threads. I tried:
<code>import threading
threading.stack_size(67108864)
threading.Thread(target=func1).start()
threading.Thread(target=func2).start()
</code>
But it doesn't work.
How to run two threads in parallel with <code>threading</code>?


A:

<code>import threading
from queue import Queue
from threading import Thread
import time


def func1():
    while True:
        print('func1')
        time.sleep(1)


def func2():
    while True:
        print('func2')
        time.sleep(1)


def worker():
    while True:
        item = q.
