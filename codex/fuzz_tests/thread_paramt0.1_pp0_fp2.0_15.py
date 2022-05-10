import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(1000000))))).start()

# Пример использования модуля threading
import threading
import time

def worker():
    """thread worker function"""
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

# Пример использования модуля threading
import threading
import time

def worker():
    """thread worker function"""
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')

def my_service():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(3)
