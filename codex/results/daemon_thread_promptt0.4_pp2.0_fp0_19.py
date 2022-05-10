import threading
# Test threading daemon

class TestThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(TestThread, self).__init__(*args, **kwargs)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            print('Test')
            time.sleep(1)

TestThread()
while True:
    print('Main')
    time.sleep(1)

# Test threading non-daemon

class TestThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(TestThread, self).__init__(*args, **kwargs)
        self.start()
    def run(self):
        while True:
            print('Test')
            time.sleep(1)

TestThread()
while True:
    print('Main')
    time.sleep(1)
</code>
Output:
<code>Main
Test
Main
Test
Main
Test
Main
Test
Main
Test
Main
Test
Main
