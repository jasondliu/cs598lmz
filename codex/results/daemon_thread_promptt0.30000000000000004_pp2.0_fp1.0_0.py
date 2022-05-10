import threading
# Test threading daemon

def test_thread(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(name, ":", time.ctime(time.time()))

def test_thread_daemon(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(name, ":", time.ctime(time.time()))

try:
    t1 = threading.Thread(target=test_thread, args=("Thread-1", 2))
    t2 = threading.Thread(target=test_thread_daemon, args=("Thread-2", 4))
    t1.start()
    t2.start()
    t2.join()
    print("End Main Thread")
except:
    print("Error: unable to start thread")
