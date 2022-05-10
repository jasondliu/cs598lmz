import threading
# Test threading daemon

class Worker(threading.Thread):
    def __init__(self, name, interval):
        threading.Thread.__init__(self)
        self.name = name
        self.interval = interval
        self.daemon = True
        self.start()
    def run(self):
        while True:
            print(self.name)
            time.sleep(self.interval)

Worker('aaa', 3)
Worker('bbb', 2)

while True:
    pass
