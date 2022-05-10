import sys, threading

def run():
    cnt = 0
    for i in range(100000000):
        cnt += 1
    print('imep %s'%threading.current_thread().name)

t1 = threading.Thread(target=run, name='ChildThread1')
t2 = threading.Thread(target=run, name='ChildThread2')

# t1.setDaemon(True)   # 设置后：t1为守护线程，无论主线程有没有完毕，t1都会结束
# t1.start()
# t2.start()

# t2.join()
# # t1.join()
# print('imep %s'%threading.current_thread().name)

# import time
# for i in range(2):
#     print('Thread({}): {}'.format(i, time.ctime()))
#     time.sleep(2)

