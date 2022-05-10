import threading
# Test threading daemon
class TestThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.thread_stop = False

    def run(self):
        print 'thread1'
        while not self.thread_stop:
            time.sleep(1)
        print 'thread1 entered stop loop'
        print 'thread2'
        while not self.thread_stop:
            time.sleep(1)
        print 'thread2 entered stop loop'
        print 'thread3'
        while not self.thread_stop:
            time.sleep(1)
            if self.thread_stop:
                print 'thread3 enter stop loop'
        print 'thread4'
        while not self.thread_stop:
            time.sleep(1)
            if self.thread_stop:
                print 'thread4 enter stop loop'

    def stop(self):
        self.thread_stop = True

tt = TestThread()
tt.setDaemon(True)
tt.start()
time.sleep(1)
tt.stop()

