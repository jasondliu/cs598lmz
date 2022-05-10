import threading
# Test threading daemon
# def worker():
#     print 'Worker'
#     return
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker)
#     t.setDaemon(True)
#     t.start()
#     threads.append(t)
#
# for t in threads:
#     t.join()


import time
import threading

class myThread(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name
        print_time(self.name, self.counter, 5)
        print "Exiting " + self.name

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
