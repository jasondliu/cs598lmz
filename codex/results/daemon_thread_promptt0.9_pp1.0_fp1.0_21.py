import threading
# Test threading daemon mode
class Th(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(True)

    def run(self):
        print 'Start:', threading.current_thread()
        for i in range(10):
            print i,
            time.sleep(0.2)
        print
        print 'Exiting:', threading.current_thread()

th = Th()
th.start()

for i in range(10):
        print 'x',
        time.sleep(0.3)
print
print 'End:', threading.current_thread()
