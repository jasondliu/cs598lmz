import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    
    def run(self):
        global count, mutex
        threadname = threading.currentThread().getName()
        
        for x in xrange(0, 1000000):
            mutex.acquire()
            count += 1
            mutex.release()
        print threadname, count

if __name__ == '__main__':
    count = 0
    mutex = threading.Lock()
    threads = []
    
    for x in xrange(0, 10):
        thread = MyThread(str(x))
        thread.setDaemon(True)
        threads.append(thread)
    
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()
        
    print "main thread: ", count

# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self
