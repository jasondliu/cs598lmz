import threading
# Test threading daemon
class MyThread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        time.sleep(1)
        print "Value send",self.h

thread1 = MyThread(1)
thread1.start()

threading.currentThread().getName()

thread1.join()

import theading

threading.main_thread()

import datetime
i = datetime.datetime.now()
