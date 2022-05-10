import sys, threading

def run():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=run, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# 因为任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线
