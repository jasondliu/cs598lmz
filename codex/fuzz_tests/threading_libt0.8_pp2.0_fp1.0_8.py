import threading
threading.
from multiprocessing import Process, Queue
def test():
    print("OK")
def f(q):
    q.put([42, None, 'hello'])
if __name__=='__main__':
    q = Queue()
    #p = Process(target=f, args=(q,))
    p=Process(target=test)
    p.start()
    p.join()
    print(q.get())    # prints "[42, None, 'hello']"

import time, threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name
