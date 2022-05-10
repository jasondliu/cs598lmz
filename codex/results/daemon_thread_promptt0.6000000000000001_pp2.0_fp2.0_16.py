import threading
# Test threading daemon
import time

class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print("running on number: %s" % self.num)
        time.sleep(3)


if __name__ == '__main__':
    t1 = MyThread(1)
    t1.start()
    print('main thread')
