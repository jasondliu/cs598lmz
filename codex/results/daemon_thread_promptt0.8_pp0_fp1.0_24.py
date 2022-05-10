import threading
# Test threading daemon

def loadsleep():
    time.sleep(3)

# Define two threads as follows
class LoadSleep(threading.Thread):
    def __init__(self, threadname, method):
        threading.Thread.__init__(self, name=threadname)
        self.method = method

    def run(self):
        self.method()


t1 = LoadSleep("Thread-1", loadsleep)
t1.start()
t1.join()
print t1.isAlive()
print "Exiting Main Thread"
