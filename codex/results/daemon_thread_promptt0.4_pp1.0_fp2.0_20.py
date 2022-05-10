import threading
# Test threading daemon
import time
import json
import requests

#
#
#
class TestThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.stop_event = threading.Event()
        self.daemon = True

    def stop(self):
        self.stop_event.set()

    def stopped(self):
        return self.stop_event.is_set()

    def run(self):
        while not self.stopped():
            print("TestThread #{}".format(self.id))
            time.sleep(1)

#
#
#
class TestThreadDaemon(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.stop_event = threading.Event()
        self.daemon = True

    def stop(self):
        self.stop_event.set()

    def stopped(self):
        return self.stop
