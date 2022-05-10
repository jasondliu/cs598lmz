import threading
# Test threading daemon
import queue

q = queue.Queue()

class TestThread(threading.Thread):
    def __init__(self, q):
        super(TestThread,self).__init__()
        self.daemon = True
        self.q = q

    def run(self):
        while True:
            print('trying to get stuff')
            if not self.q.empty():
                thing = self.q.get()
                print('got it')


class Foo:
    def __init__(self):
        self.q = queue.Queue()
        self.test_thread = TestThread(self.q)
        self.test_thread.start()

    def run(self):
        self.q.put(1)
        self.q.put(2)
        self.q.put(3)

    def finish(self):
        self.q.put('END')

if __name__ == '__main__':
    f = Foo()
    f.run()
    time.sleep(2)
    f.finish()
    print('
