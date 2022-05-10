import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread2\n')).start()

# Run code concurrently with the concurrent.futures module
import concurrent.futures
def task(n):
    return (n, n/10, n*2)

ex = concurrent.futures.ThreadPoolExecutor(max_workers=2)
print('main: starting')
f = ex.submit(task, 5)
print('main: future:', f)
print('main: waiting for results')
result = f.result()
print('main: result:', result)

# Concurrent execution in the standard library
from time import sleep, strftime
from concurrent import futures

def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)

def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s...'
