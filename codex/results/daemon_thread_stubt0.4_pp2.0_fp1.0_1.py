import sys, threading

def run():
    while True:
        print('thread %s is running...' % threading.current_thread().name)
        time.sleep(1)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=run, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)


# 分析：
# 1. 当主线程退出的时候，子线程kill掉
# 2. 子线程是否独立运行，与父子线程没有关系
# 3. join()方法可以等待子线程结束后再继续往下运行，通常
