import sys, threading

def run():
    lock = threading.Lock()
    k = 0
    while True:
        print 1
        lock.acquire()
        k += 1
        print k
        lock.release()

thread = threading.Thread(target=run)
thread.start()

while True:
    print 2
