import sys, threading

def run():
    print 'Thread %s is running...' % threading.current_thread().getName()

def test():
    print 'Thread %s is running...' % threading.current_thread().getName()
    t = threading.Thread(target=run, name='LoopThread')
    t.start()
    t.join()
    print 'Thread %s ended.' % threading.current_thread().getName()

if __name__ == '__main__':
    test()
