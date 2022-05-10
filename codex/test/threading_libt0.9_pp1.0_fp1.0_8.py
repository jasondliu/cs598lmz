import threading
threading.current_thread().name

# Using the Timer
from threading import Timer
t = Timer(5,print(threading.current_thread().name))
t.start()
t.join()

# Subclassing the Thread Class
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        print(threading.currentThread().getName(),'Start')
        time.sleep(3)
        print(threading.currentThread().getName(),'Exits')
        
for x in range(4):
    mythread = MyThread()
    mythread.start()
    time.sleep(1)
    
threading.current_thread().name
threading.enumerate()

# The Treading Synchronization Modules
import logging
import threading
import time

def thread_function(name):
    logging.info(f'Thread {name}:starting')
    time.sleep(2)
    logging.info(f'Thread {name}:finishing')
    
