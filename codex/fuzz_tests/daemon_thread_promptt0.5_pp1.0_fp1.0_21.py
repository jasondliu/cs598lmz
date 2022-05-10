import threading
# Test threading daemon

# To run:
# python3 -m pytest test_threading_daemon.py

def test_threading_daemon():
    # Test threading daemon
    import threading
    import time
    import os

    class TestThread(threading.Thread):
        def __init__(self, *args, **kwargs):
            super(TestThread, self).__init__(*args, **kwargs)
            self.daemon = True

        def run(self):
            time.sleep(1)
            print("I'm done.")

    t = TestThread()
    t.start()
    t.join()
    assert os.getpid() == os.getppid()


if __name__ == "__main__":
    test_threading_daemon()
