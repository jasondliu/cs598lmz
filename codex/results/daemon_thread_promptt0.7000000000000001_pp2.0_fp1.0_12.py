import threading
# Test threading daemon
class TestDaemon(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(TestDaemon, self).__init__(*args, **kwargs)
        self.daemon = True
        self.stop = threading.Event()

    def run(self):
        while not self.stop.wait(2): # Call wait() every 2 seconds
            print "I'm a daemon and I'm still active!"

    def join(self, *args, **kwargs):
        self.stop.set()
        super(TestDaemon, self).join(*args, **kwargs)

if __name__ == '__main__':
    import time
    t = TestDaemon()
    t.start()
    time.sleep(1)
    t.join()
</code>

