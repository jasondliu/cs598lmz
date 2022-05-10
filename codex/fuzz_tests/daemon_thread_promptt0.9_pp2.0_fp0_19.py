import threading
# Test threading daemon
#

class Test(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        while True:
            print "hello"
            time.sleep(5)
if __name__ == "__main__":
    a = Test()
    a.start()
    time.sleep(2)
    print 'aa'
    time.sleep(3)
    print 'bb'
    time.sleep(4)
    print "cc"
