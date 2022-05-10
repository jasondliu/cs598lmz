import threading
# Test threading daemon flag
def daemon():
    print('Starting:', threading.currentThread().getName())
    time.sleep(2)
    print('Exiting:', threading.currentThread().getName())

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Starting:', threading.currentThread().getName())
    print('Exiting:', threading.currentThread().getName())

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# Test threading.Timer
def hello():
    print('hello, world')

t = threading.Timer(3.0, hello)
t.start()

# Test threading.Thread
class MyThread(threading.Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        print('Thread:', self.name)
