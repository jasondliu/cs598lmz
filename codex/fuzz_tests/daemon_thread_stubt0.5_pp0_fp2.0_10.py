import sys, threading

def run():
    #print 'thread %s is running...' % threading.current_thread().name
    sys.stdout.write('thread %s is running...\n' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        #print 'thread %s >>> %s' % (threading.current_thread().name, n)
        sys.stdout.write('thread %s >>> %s\n' % (threading.current_thread().name, n))
        time.sleep(1)
    #print 'thread %s ended.' % threading.current_thread().name
    sys.stdout.write('thread %s ended.\n' % threading.current_thread().name)

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=run, name='MyThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name
