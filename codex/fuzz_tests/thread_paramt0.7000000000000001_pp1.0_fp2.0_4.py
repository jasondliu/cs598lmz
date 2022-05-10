import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello world!\n')).start()

def print_hello(): 
    # function to be executed in a thread 
    print("Hello World")

# creating thread 
t = threading.Thread(target=print_hello)  

# starting thread 
t.start() 

print("\n")

from threading import Thread
def square(n):
    print(n)

th = []
for i in range(10):
    t = Thread(target=square, args=(i,))
    th.append(t)
    t.start()

print("\n")

from threading import Thread
from time import sleep

def my_func():
    print('sleeping 5 sec from thread %s' % threading.currentThread().getName())
    sleep(5)
    print('finished sleeping from thread %s' % threading.currentThread().getName())

if __name__ == '__main__':
    t = Thread(name='my_service', target=my_func)
    t.start()
