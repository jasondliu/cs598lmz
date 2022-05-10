import threading
threading.Thread(target=lambda: print(1)).start()

# 3. 创建多个线程
def print_1():
    print(1)

t = Thread(target=print_1)
t.start()

'''
所有的线程都被创建为Daemon，必须手动设置为False，才能保证线程不是Daemon。
只要还有一个非Daemon线程活着，Python解释器就不会关闭。

'''
def print_even(n):
    while n > 0:
        if n % 2 == 0:
            print(n)
        n -= 1

def print_odd(n):
    while n > 0:
        if n % 2 != 0:
            print(
