import threading
# Test threading daemon
 
class MyThread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
 
    def run(self):
        print('Thread', self.threadID, 'starts')
        while True:
            time.sleep(3)
            print('Thread', self.threadID, 'alive')
 
if __name__ == '__main__':
    thread1 = MyThread(1)
    thread2 = MyThread(2)
    thread2.setDaemon(True)
    thread1.start()
    thread2.start()
    thread1.join()
    print('Thread1 ended')
    print('Thread2 ended')
