import sys, threading

def run():
    print('thread %s is running...' % threading.current_thread().name)
    for i in range(5):
        print(i)
        time.sleep(1)

print('thread %s is running...' % threading.current_thread().name)

# 创建子线程
t = threading.Thread(target=run, name='T1')
t.start()
t.join()

print('thread %s ended.' % threading.current_thread().name)
