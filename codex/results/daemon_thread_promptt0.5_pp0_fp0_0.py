import threading
# Test threading daemon
#
# Author: Howard Webb
# Date: 6/23/2017

from time import sleep

class MyThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self._id = id
        self._stop = threading.Event()
        
    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()
        
    def run(self):
        print "Starting thread: ", self._id
        while not self.stopped():
            print "Thread: ", self._id
            sleep(1)
        print "Exiting thread: ", self._id

if __name__=="__main__":
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()
    sleep(5)
    t1.stop()
    t2.stop()
