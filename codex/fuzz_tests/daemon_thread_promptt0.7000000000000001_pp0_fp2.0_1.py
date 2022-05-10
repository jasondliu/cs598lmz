import threading
# Test threading daemon
import time

class MyThread(threading.Thread):
    def __init__(self,threadName):
        threading.Thread.__init__(self, name = threadName)
        self.threadName = threadName
        self.running = True

    def terminate(self):
        self.running = False
        self.join()

    def run(self):
        while self.running:
            print(self.threadName)
            time.sleep(2)

if __name__ == '__main__':
    t = MyThread('t1')
    t.setDaemon(True)
    t.start()
    time.sleep(10)
    t.terminate()
