import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

#2.
import threading

def add(a, b):
    return a + b

def print_sum(a, b):
    print('{} + {} = {}'.format(a, b, add(a, b)))

def print_hello():
    print('Hello!')

threading.Thread(target=print_hello).start()
threading.Thread(target=print_sum, args=(1, 2)).start()

#3.
import threading

def print_sum(a, b):
    print('{} + {} = {}'.format(a, b, a + b))

def print_hello():
    print('Hello!')

threading.Thread(target=print_sum, args=(1, 2)).start()
threading.Thread(target=print_sum, args=(3, 4)).start()
