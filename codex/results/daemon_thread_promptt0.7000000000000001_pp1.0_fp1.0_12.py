import threading
# Test threading daemon
class Threading_daemon(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.thread_num = num

    def run(self):
        global res
        threadname = threading.currentThread().getName()
        res += 1
        print("thread %d result:%d" % (self.thread_num, res))
        print("Thread %s: finishing" % threadname)

if __name__ == '__main__':
    res = 0
    thread1 = Threading_daemon(1)
    thread1.setDaemon(True)
    thread2 = Threading_daemon(2)
    thread3 = Threading_daemon(3)
    thread2.setDaemon(True)
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
    print("Main thread done!")
