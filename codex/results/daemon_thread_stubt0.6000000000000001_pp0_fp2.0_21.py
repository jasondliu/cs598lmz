import sys, threading

def run():
    print 'Hello from thread %s' % threading.currentThread().getName()
    return

threading.Thread(target=run).start()

time.sleep(0.1)

print 'Hello from thread %s' % threading.currentThread().getName()
