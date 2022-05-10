import threading
# Test threading daemon
# https://docs.python.org/2/library/threading.html#thread-objects

class ThreadClass(threading.Thread):
    def run(self):
        print "Thread %s started" % self.getName()
        for i in range(10):
            print "Thread %s, count %d" % (self.getName(), i)
            time.sleep(0.5)
        print "Thread %s finished" % self.getName()

def main():
    for i in range(3):
        t = ThreadClass()
        t.setDaemon(True)
        t.start()

    print "Main thread finished"

if __name__ == "__main__":
    main()
