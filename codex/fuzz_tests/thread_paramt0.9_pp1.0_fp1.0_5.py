import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread 2\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread 3\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread 4\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread 5\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread 6\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread 7\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread 8\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread 9\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread 10\n')).start()
# print('Thread 1')

import threading, itertools
def spin(msg, done):
 for char in itertools.cycle('|/-\\'):

