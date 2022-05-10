import sys, threading

def run():
    global running
    global count
    global lock

    while running:
        lock.acquire()
        count = count + 1
        lock.release()

running = True
count = 0

lock = threading.Lock()

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run)

t1.start()
t2.start()

time.sleep(1)

running = False

t1.join()
t2.join()

print(count)
