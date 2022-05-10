import sys, threading

def run():
    while True:
        sys.stdout.write('\n'+str(threading.currentThread()))
        sys.stdout.write('\npid:%d' % os.getpid())
        print('\nname:%s' % threading.currentThread().getName())
        print('\nalive:%s' % threading.currentThread().isAlive())
        print('\ndummy:%s' % threading.currentThread().isDaemon())
        print('\nident:%s' % threading.currentThread().ident)
        print('\nnumber:%s' % threading.currentThread().name)
        time.sleep(1)

for i in range(10):
    t = threading.Thread(target = run)
    t.start()
    t.join()
