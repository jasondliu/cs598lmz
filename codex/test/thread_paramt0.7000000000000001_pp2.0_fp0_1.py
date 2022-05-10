import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()
"""

"""
from threading import Thread

print('hello')

def print_a():
    for i in range(100):
        print('A',end='')

def print_b():
    for i in range(100):
        print('B',end='')

thread1 = Thread(target=print_a)
thread2 = Thread(target=print_b)

thread1.start()
thread2.start()

print('bye')
