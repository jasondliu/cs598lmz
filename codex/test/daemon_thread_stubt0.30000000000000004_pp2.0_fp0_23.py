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

# 创建Thread的实例，传给它一个函数
# 如果要启动一个子线程就必须调用start()方法，这会让线程开始执行run()方法
# join()方法可以等待子线程结束后再继续往下运行，通常
