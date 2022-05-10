import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()

# from multiprocessing import Process
# def f(name):
#     print('hello', name)
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()

# from multiprocessing import Pool
# def f(x):
#     return x*x
#
# if __name__ == '__main__':
#     with Pool(5) as p:
#         print(p.map(f, [1, 2, 3]))

# import time
# import os
#
# def foo():
#     print('in foo() pid=%s, ppid=%s' % (os.getpid(), os.getppid()))
#     time.sleep(1)
#
# if __name__ == '__main__
