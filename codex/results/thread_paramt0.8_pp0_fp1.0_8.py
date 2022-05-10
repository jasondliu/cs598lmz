import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from another thread!\n')).start()

def countdown(n):
    while n > 0:
        n -= 1

import multiprocessing
print('Number of CPUs:', multiprocessing.cpu_count())

def f(x):
    print('{} is running'.format(x))
    return [x*x]
if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=20)
    result = pool.map(f, range(5))
    print(result)
