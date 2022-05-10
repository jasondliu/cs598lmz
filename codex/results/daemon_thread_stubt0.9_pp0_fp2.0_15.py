import sys, threading

def run():
    print 'Thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'Thread %s >>> %s' % (threading.current_thread().name, n)
    print 'Thread %s ended.' % threading.current_thread().name

print 'Thread %s is running...' % threading.current_thread().name
t = threading.T
