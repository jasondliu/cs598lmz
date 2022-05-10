import threading
# Test threading daemon
import time

# This thread runs on a separate thread and should clean up after itself
class TestThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        self.test_args = kwargs['test_args']
        super(TestThread, self).__init__(*args, **kwargs)

    def run(self):
        print 'I am a test thread'
        print self.test_args
        while True:
            time.sleep(1)

# Create a thread
test_thread = TestThread(name='Test Thread', test_args='test')
# Daemonize it
test_thread.daemon = True
# Start it
test_thread.start()

# Loop forever
while True:
    time.sleep(1)
