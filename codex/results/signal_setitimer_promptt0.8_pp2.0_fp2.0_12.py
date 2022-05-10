import signal
# Test signal.setitimer() and signal.setitimer()
import sys
import os
import queue
import threading
def handler(a, b):
    print('handler', a, b)
class MyThread(threading.Thread):
    def __init__(self, q, n):
        super().__init__()
        self.q = q
        self.n = n
    def run(self):
        self.q.put(signal.setitimer(self.n))
        self.q.put(signal.getitimer(self.n))
        self.q.put(signal.setitimer(self.n, -1, -1))
        self.q.put(signal.getitimer(self.n))
        self.q.put(signal.setitimer(self.n, 10, 0))
        self.q.put(signal.getitimer(self.n))
        self.q.put(signal.setitimer(self.n, 1, 1))
        self.q.put(signal.getitimer(self.n
