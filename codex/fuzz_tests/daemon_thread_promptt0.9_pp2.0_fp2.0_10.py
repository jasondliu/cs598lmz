import threading
# Test threading daemon
import time

def worker( interval ) :
    t = threading.currentThread()
    whilst = True
    count = 0
    print "["+str(t.getName())+"] Start"
    while whilst:
        print "["+str(t.getName())+"] Working -" + str(count)
        count += 1
        time.sleep( interval )
        if not t.isAlive():
            whilst = False
    print "["+str(t.getName())+"] Stop"

class myThread (threading.Thread):
    def __init__(self, threadID, name, interval):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.interval = interval
    def run(self):
        print "Starting " + self.name
        worker( self.interval )
        print "Exiting " + self.name

def testfunc():
    print 'testfunc called'

def main():
    print 'main started'
    thread1 = myThread(
