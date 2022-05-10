import sys, threading

def run():
    print('Current Thread: ', threading.current_thread().name)
    sys.exit()

if __name__ == '__main__':
    print('Current Thread:', threading.current_thread().name)
    t = threading.Thread(target=run)
    t.start()
    t.join()

# 获取线程信息
import threading

def run(n):
    print('task', n)

t1 = threading.Thread(target=run, args=('t1',))
t2 = threading.Thread(target=run, args=('t2',))
t1.start()
t2.start()
print(t1.getName())
print(t2.getName())

# 指定线程名称
import threading

def run(n):
    print('task', n)

t1 = threading.Thread(target=run, args=('t1',), name='thread1')
t2 = threading
