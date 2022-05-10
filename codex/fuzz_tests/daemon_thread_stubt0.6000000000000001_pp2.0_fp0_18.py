import sys, threading

def run():
    print('Hello from thread %s' % threading.currentThread().getName())

def worker():
    """thread worker function"""
    print('Worker')
    return

t = threading.Thread(target=run)
t.start()

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
