import threading
# Test threading daemon
def test():
    while True:
        print("running")
        time.sleep(1)

daemon = threading.Thread(target=test)
daemon.setDaemon(True)
daemon.start()
time.sleep(5)
daemon.join()

# Test threading queue
def th1_func(i):
    while True:
        if q.empty():
            print("th1=%d, q is empty" % i)
            time.sleep(1)
        else:
            item = q.get()
            print("th1=%d, get item=%d" % (i, item))
            q.task_done()
            time.sleep(1)

def th2_func(i):
    while True:
        if q.full():
            print("th2=%d, q is full" % i)
            time.sleep(1)
        else:
            item = i % 10
            q.put(item)
            print("th2=%d, put item=%d" % (i, item
