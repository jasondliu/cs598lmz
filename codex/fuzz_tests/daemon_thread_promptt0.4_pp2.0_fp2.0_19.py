import threading
# Test threading daemon
import time

#def loop():
#    print('thread %s is running...' % threading.current_thread().name)
#    n = 0
#    while n < 5:
#        n = n + 1
#        print('thread %s >>> %s' % (threading.current_thread().name, n))
#        time.sleep(1)
#    print('thread %s ended.' % threading.current_thread().name)
#
#print('thread %s is running...' % threading.current_thread().name)
#t = threading.Thread(target=loop, name='LoopThread')
#t.start()
#t.join()
#print('thread %s ended.' % threading.current_thread().name)

# Test threading lock
#balance = 0
#lock = threading.Lock()
#
#def change_it(n):
#    global balance
#    balance = balance + n
#    balance = balance - n
#
#def run_thread(n):
#    for i in range(100000):
#
