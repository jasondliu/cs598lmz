import weakref
import threading
import time
import logging

# TODO:
# - Don't do the busy loop in the main thread.
# - Don't do the busy loop in the worker thread.
# - Use a different event loop for the worker thread.
# - Use a different event loop for the main thread.

def log(msg):
    logging.info(msg)

def wlog(msg):
    logging.info("worker: " + msg)

class Worker:
    def __init__(self):
        self.mutex = threading.Lock()
        self.cond = threading.Condition(self.mutex)
        self.result = None
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def run(self):
        wlog("started")
        while True:
            wlog("waiting for work")
            with self.cond:
                self.cond.wait()
                work = self.work
                self.work = None

            self.result = work()
            wlog("finished work")
           
