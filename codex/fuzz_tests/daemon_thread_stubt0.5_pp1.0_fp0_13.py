import sys, threading

def run():
    print "Starting " + threading.currentThread().getName()
    sys.exit(0)

class ExitThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print "Starting " + self.getName()
        sys.exit(0)

def test(count):
    for i in range(count):
        t = ExitThread()
        t.start()
        t.join()

test(5)
