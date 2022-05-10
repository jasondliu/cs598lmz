import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input("입력 : "))).start()
# # 입력 : hello
# hello
# import threading
#
# def worker(num):
#     """thread worker function"""
#     print('Worker: %s' % num)
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     threads.append(t)
#     t.start()
#
# # Worker: 4
# # Worker: 2
# # Worker: 3
# # Worker: 1
# # Worker: 0

import threading
import time

def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')

def my_service():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(3)
