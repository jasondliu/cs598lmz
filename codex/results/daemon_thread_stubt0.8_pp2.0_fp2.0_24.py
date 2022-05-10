import sys, threading

def run():
    print('thread %s is running...' % threading.current_thread().name)

if __name__ == '__main__':
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=run, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)

# 多线程还有一个优势是可以利用多核CPU，多线程的并发在一定程度上可以提高程序的执行效率。

# 由于CPU执行代码都是顺序执行的，除非有多个CPU，否则任何一个线
