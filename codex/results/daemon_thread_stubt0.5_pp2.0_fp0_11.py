import sys, threading

def run():
    print('Thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('Thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('Thread %s ended.' % threading.current_thread().name)

print('Thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=run, name='LoopThread')
t.start()
t.join()
print('Thread %s ended.' % threading.current_thread().name)

# balance = 0
# lock = threading.Lock()
#
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(1000000):
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#            
