import threading
# Test threading daemon
class MyThread(threading.Thread):
    def __init__(self, name, interval):
        threading.Thread.__init__(self)
        self.name = name
        self.interval = interval
        self.thread_stop = False
    def run(self):
        print("%s started" %self.name)
        count = 0
        while not self.thread_stop:
            count += 1
            time.sleep(self.interval)
        print("%s stopped at %s" %(self.name, count))
    def stop(self):
        print("%s stopped" %self.name)
        self.thread_stop = True
def test():
    t1 = MyThread("Thread-1", 1)
    t1.setDaemon(True)
    t1.start()
    t2 = MyThread("Thread-2", 1)
    t2.setDaemon(True)
    t2.start()
    t1.stop()
    t2.stop()
    print("main thread stopped")
if __name__ == "
