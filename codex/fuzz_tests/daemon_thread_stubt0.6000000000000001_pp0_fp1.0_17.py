import sys, threading

def run():
    print('Thread %s started' % threading.current_thread().name)
    sys.stdout.flush()
    time.sleep(0.1)
    print('Thread %s finished' % threading.current_thread().name)
    sys.stdout.flush()

def test():
    for i in range(5):
        t = threading.Thread(target=run)
        t.start()
    print('Thread %s finished' % threading.current_thread().name)
    sys.stdout.flush()

test()
