import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread\n')).start()

"""
Write a program to create a thread and check for synchronization among the threads using
threading module.
"""

import threading as th
import time
def display():
    print('Thread name is',th.current_thread().getName())
    time.sleep(5)
    print('thread execution completed')

for i in range(5):
    t=th.Thread(target=display)
    time.sleep(1)
    t.start()
    time.sleep(1)
    t.join()
    print('Main thread executed')
