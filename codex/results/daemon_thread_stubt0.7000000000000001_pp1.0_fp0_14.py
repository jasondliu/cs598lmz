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

# threading.current_thread():返回当前线程的实例
