import sys, threading

def run():
    global counter, lock
    while True:
        lock.acquire()
        if counter < 10:
            counter += 1
            print counter
            lock.release()
        else:
            lock.release()
            sys.exit(0)

lock = threading.Lock()
counter = 0

for i in range(10):
    t = threading.Thread(target=run)
    t.start()
