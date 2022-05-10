import threading
# Test threading daemon
# https://docs.python.org/3/library/threading.html

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.daemon = True

    def run(self):
        print('Thread %s started' % self.name)
        while True:
            print('Thread %s is running' % self.name)
            time.sleep(0.5)

if __name__ == '__main__':
    t1 = MyThread('A')
    t2 = MyThread('B')
    t1.start()
    t2.start()
    time.sleep(1)
    print('Main done')
