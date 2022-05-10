import sys, threading

def run():
    while True:
        print('thread %s is running...' % threading.current_thread().name)
        time.sleep(1)

if __name__ == '__main__':
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=run, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)

# threading.current_thread()返回当前线程的实例。threading.Thread()方法用来构造一个线程实例，
# 该实例调用start()后，会调用该实例target指向的函数（本例即run()）。

# 我们需
