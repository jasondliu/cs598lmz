import threading
# Test threading daemon

class ThreadingTest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.daemon = True
    def run(self):
        while True:
            print("ThreadingTest-%s" % self.name)
            time.sleep(1)

threads = []
for i in range(5):
    t = ThreadingTest(i)
    t.start()
    threads.append(t)

time.sleep(5)
print("Main Thread exit")
