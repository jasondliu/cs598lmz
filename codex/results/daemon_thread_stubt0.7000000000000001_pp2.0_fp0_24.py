import sys, threading

def run():
    for i in range(1, 99999):
        print('thread %s is running...' % threading.current_thread().name)
        sys.stdout.flush()
        time.sleep(1)
    print('thread %s is ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=run, name='MyThread')
t.start()
t.join()
print('thread %s is ended.' % threading.current_thread().name)

# 分析：
# 子线程执行完毕后，主线程才结束
