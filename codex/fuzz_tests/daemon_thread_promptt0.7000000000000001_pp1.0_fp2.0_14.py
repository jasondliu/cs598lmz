import threading
# Test threading daemon
class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num
    def run(self):
        print "Starting " + self.num
        time.sleep(5)
        print "Exiting " + self.num

print "Starting Main Thread"

thread1 = MyThread("A")
thread1.start()

thread2 = MyThread("B")
thread2.start()

print "Exiting Main Thread"


'''
class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num
    def run(self):
        print "Starting " + self.num
        time.sleep(5)
        print "Exiting " + self.num

print "Starting Main Thread"

thread1 = MyThread("A")
thread1.start()

thread2 = MyThread("B")
thread2.start()

thread1.join()
thread
