import threading
# Test threading daemon
class MyDaemonThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
        self.thread_stop = False

    def run(self) :
        print "Starting " + self.name
        self.MyPrint(self.name, self.delay, 5)
        print "Exiting " + self.name
    
    def MyPrint(self, threadName, delay, counter):
        while counter:
            if self.thread_stop:
                return
            time.sleep(delay)
            print "%s: %s" % (threadName, time.ctime(time.time()))    
            counter -= 1

    def stop(self):
        self.thread_stop = True

def test_thread_daemon() :
    # Create new threads
    thread2 = MyDaemonThread(2, "Thread-2", 2)
    thread1 = MyDaemonThread(1, "
