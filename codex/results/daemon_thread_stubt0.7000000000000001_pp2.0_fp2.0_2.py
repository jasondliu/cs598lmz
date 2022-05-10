import sys, threading

def run():
    #print 'Thread Started'
    sys.stdout.write('Hello from thread %s\n' % threading.currentThread())

def run2():
    #print 'Thread Started'
    sys.stdout.write('Hello from thread %s\n' % threading.currentThread())

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run2)

sys.stdout.write('Hello from main thread\n')

t1.start()
t2.start()

t1.join()
t2.join()

sys.stdout.write('Hello from main thread\n')
