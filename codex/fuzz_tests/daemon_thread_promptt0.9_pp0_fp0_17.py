import threading
# Test threading daemon
class maThread(threading.Thread):
    def __init__(self,Num):
        threading.Thread.__init__(self)
        if Num == 12:
            threading.Thread.setDaemon(self,True)
        
    def run(self):
        while threading.activeCount() == 3:
            print threading.activeCount()
            print self
        print threading.currentThread()
        print 1234
        
Th = maThread(12)
Th2 = maThread(12)

Th.start()   
Th2.start()
print "tttttttttttttttttttttttttttttt"
threading.Event().wait(10)
print "tttttttttttttttttttttttttttttt"
