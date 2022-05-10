import threading
# Test threading daemon
#
#
class TestThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.thread_num = num

    def run(self):
        global count, mutex
        threadname = threading.currentThread().getName()

        for x in range(0, int(1e7)):
            mutex.acquire()
            count += 1
            mutex.release()
        print("thread %s ended, count = %d \n" % (threadname, count))

if __name__ == "__main__":
    count = 0
    mutex = threading.Lock()
    threads = []
    for x in range(0, 2):
        threads.append(TestThread(x))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("main thread ended, count = %d \n" % count)
