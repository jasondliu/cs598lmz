import threading
threading.current_thread()

#Create a Thread object
t = threading.Thread()
t.start()

#Create a Thread object and override its run() method
class mythread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        print "Value send", self.h

thread1 = mythread(1)
thread1.start()
