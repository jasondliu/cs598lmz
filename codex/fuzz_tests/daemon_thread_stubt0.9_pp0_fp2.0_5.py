import sys, threading

def run():
    return 'hello from worker thread'

threads = 3

def worker():
    """thread worker function"""
    print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worke
