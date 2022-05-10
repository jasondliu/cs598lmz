import sys, threading

def run():
    for i in range(50):
        print 'i: {}, thread: {}'.format(i, threading.currentThread().getName())
        time.sleep(1. / 10)

def main():
    thread_pool = []
    for i in range(4):
        t = threading.Thread(target=run, name='thread {}'.format(i))
        t.daemon = True
        t.start()
        thread_pool.append(t)

    while True:
        print 'running threads: {}'.format(threading.activeCount())
        print 'current thread: {}'.format(threading.currentThread().getName())
        time.sleep(1. / 3)
        alive = False
        for t in thread_pool:
            alive = alive or t.isAlive()
        if not alive:
            break

if "__main__" == __name__:
    sys.exit(main())
