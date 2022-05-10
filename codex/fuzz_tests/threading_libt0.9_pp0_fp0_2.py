import threading
threading.enumerate()
"""
#threading.active_count()

def fib(n):
    """ Print a Fibonacci series to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    #return a
    
    
def call(method,args):
    return method(*args)

#noarg=call(print,'hi')
#print("return from call noargs "+str(noarg))

from threading import Thread
t = Thread(target=fib, args=(10,))
#t.start()
#print("return from Thread "+str(t))

import threading
threading.enumerate()

import multiprocessing
multiprocessing.cpu_count()
t = multiprocessing.Process(target=fib, args=(10,))
#t.start()

#t.is_alive()
#t.terminate()
#t.is_alive()

#run
