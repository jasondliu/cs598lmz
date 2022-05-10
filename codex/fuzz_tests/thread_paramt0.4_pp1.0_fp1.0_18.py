import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# 从控制台读取
# import sys
# def spin(msg, done):
#     write, flush = sys.stdout.write, sys.stdout.flush
#     for char in msg:
#         write(char)
#         flush()
#         write('\x08'*len(msg))
#     done.set()
# done = threading.Event()
# s = threading.Thread(target=spin, args=('thinking!', done))
# s.start()
# done.wait()
# s.join()
# print('Spinned!');

# 使用锁和条件变量
# import threading
# class PeriodicTimer:
#     def __init__(self, interval):
#         self._interval = interval
#         self._flag = 0

