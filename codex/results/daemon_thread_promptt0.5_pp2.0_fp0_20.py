import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print "starting " + str(self.num)
        time.sleep(5)
        print "exiting " + str(self.num)

thread1 = MyThread(1)
thread1.setDaemon(True)
thread1.start()

print "Main thread exiting"

# thread1.join()

time.sleep(10)

print "Main thread exiting"
