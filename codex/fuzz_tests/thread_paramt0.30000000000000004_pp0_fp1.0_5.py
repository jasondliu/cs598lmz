import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello World\n')).start()

# 创建一个线程
def thread_job():
    print('This is an added Thread, number is %s' % threading.current_thread())

def main():
    added_thread = threading.Thread(target=thread_job,)
    added_thread.start()

if __name__ == '__main__':
    main()

# 创建多个线程
import threading
import time

def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')

def T2_job():
    print('T2 start\n')
    print('T2 finish\n')

def main():
    added_thread = threading.Thread(target=thread_job,)
    thread2 = threading.Thread(target=T2_job,)
    added_thread.start()
