import threading
# Test threading daemon status
if __name__ == "__main__":
    print(threading.current_thread().daemon)
    t = threading.Thread(target=lambda: None)
    print(t.isDaemon)
    print(t.daemon)

    # The Thread.isAlive() returns whether a thread object is alive (i.e. the thread hasn’t yet terminated).
    # The Thread.is_alive() is a deprecated alias for Thread.isAlive() for compatibility with Python 2.
    start = datetime.datetime.now()
    def myrun(k):
        for x in range(10000):
            for j in range(1000):
                k += 1
        print(k)
    
    import time 
    for k in range(10):
        t = threading.Thread(target=lambda: myrun(0))
        t.start()
    print(threading.enumerate())
    time.sleep(2)
    print(threading.enumerate())
    print(t.is_alive())
    t.join()

