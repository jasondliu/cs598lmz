import threading
# Test threading daemon

class TestThreading(threading.Thread):
    instance = None

    def __init__(self):
        threading.Thread.__init__(self)
        if TestThreading.instance is None:
            TestThreading.instance = self

    def run(self):
        print("Thread started!")
        while True:
            print("Thread running")
            time.sleep(10)

    def stop(self):
        TestThreading.instance = None

TestThreading().run()
