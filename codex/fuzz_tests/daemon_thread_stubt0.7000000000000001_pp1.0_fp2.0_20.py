import sys, threading

def run():
    print "Hello from thread %s" % threading.currentThread().getName()

if __name__ == '__main__':
    print "Hello from thread %s" % threading.currentThread().getName()
    for i in range(5):
        t = threading.Thread(target=run)
        t.start()
