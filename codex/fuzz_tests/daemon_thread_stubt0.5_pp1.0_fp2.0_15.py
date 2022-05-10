import sys, threading

def run():
    for i in range(4):
        print('Thread %s is running...' % threading.current_thread().name)
        time.sleep(1)
    print('Thread %s ended.' % threading.current_thread().name)

print('Thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=run, name='LoopThread')
t.start()
t.join()
print('Thread %s ended.' % threading.current_thread().name)

# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所
