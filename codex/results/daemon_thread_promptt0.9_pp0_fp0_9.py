import threading
# Test threading daemon
class DaemonThread(threading.Thread):
    def __init__(self, v):
        threading.Thread.__init__(self)
        self.v = v
        self.daemon = True
    def run(self):
        while True:
            print '>>>', self.v
            time.sleep(1)

dt = DaemonThread(3)
dt.start()

time.sleep(1)
print 'Main'
time.sleep(2)
print 'done'
