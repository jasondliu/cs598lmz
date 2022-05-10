import sys, threading

def run():
    t = threading.current_thread()
    for i in xrange(14):
        print "Hello from", t.getName()
        sys.stdout.flush()

a = threading.Thread(None, run)
a.start()
a.join()
