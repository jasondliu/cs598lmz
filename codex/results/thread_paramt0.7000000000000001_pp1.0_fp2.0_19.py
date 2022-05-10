import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello, world\n')).start()

# Solution 2 - using threading and lambda
import threading
threading.Thread(target=lambda x: sys.stdout.write(x), args=('Hello, world\n',)).start()

# Solution 3 - using multiprocessing
import multiprocessing, sys
multiprocessing.Process(target=lambda: sys.stdout.write('Hello, world\n')).start()

# Solution 4 - using multiprocessing and lambda
import multiprocessing
multiprocessing.Process(target=lambda x: sys.stdout.write(x), args=('Hello, world\n',)).start()

# Solution 5 - using Queue
import queue
import threading

def subproc(queue):
    queue.put("Hello, world\n")

q = queue.Queue()
t = threading.Thread(target=lambda q: subproc(q), args=(q,))
t.start()
t.join()
print(q.get())

# Solution 6 -
