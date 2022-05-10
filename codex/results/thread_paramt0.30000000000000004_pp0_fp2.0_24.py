import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(str(i) for i in range(10)))).start()

# 使用线程池
from concurrent.futures import ThreadPoolExecutor
def task(n):
    print('{} squared is {}'.format(n, n ** 2))

with ThreadPoolExecutor(max_workers=3) as pool:
    pool.map(task, range(10))

# 协程
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = yield
        if pattern in line:
            print(line)

search = grep('coroutine')
next(search)
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutine instead!")

# 协程的简单实现
def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)
