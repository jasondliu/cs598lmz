import threading
# Test threading daemon
class TestWorker(threading.Thread):
    def __init__(self, n, name='TestWorker'):
        super(TestWorker, self).__init__(name=name)
        self.n = n
        self.daemon = True
        
    def run(self):
        while True:
            print(self.name, self.n)
            time.sleep(1)

# Create a new thread
t = TestWorker(0)
t.start()

# Main thread
while True:
    print("Main")
    time.sleep(0.5)

# Main thread will never stop until t thread is stopped

# Use threading daemon
t = TestWorker(0)
t.daemon = True
t.start()

# Main thread
while True:
    print("Main")
    time.sleep(0.5)

# Main thread also stopped

# Test threading lock
class TestWorker2(threading.Thread):
    def __init__(self, n, lock, name='TestWorker2'):

