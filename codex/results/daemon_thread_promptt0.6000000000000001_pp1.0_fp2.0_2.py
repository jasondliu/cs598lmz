import threading
# Test threading daemon

class TestThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.daemon = True
    def run(self):
        while True:
            print '%s' % self.name
            time.sleep(1)

TestThread('A').start()
TestThread('B').start()

while True:
    pass

# Test multithreading

def test_func(n):
    for i in range(n):
        print i

t1 = threading.Thread(target=test_func, args=(5,))
t2 = threading.Thread(target=test_func, args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()

# Test multiprocessing

def test_func(n):
    for i in range(n):
        print i

p1 = multiprocessing.Process(target=test_func, args=(5,))
p2
