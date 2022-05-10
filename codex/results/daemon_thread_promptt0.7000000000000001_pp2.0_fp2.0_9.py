import threading
# Test threading daemon
def f():
    print('thread function')
    # print('thread function {0}'.format(threading.currentThread().getName()))  # thread function Thread-1
    return

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=f)
        t.setDaemon(True)
        t.start()
    print('main thread')
    # print('main thread {0}'.format(threading.currentThread().getName()))  # main thread MainThread

# Test threading Lock
class Counter(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increment(self):
        self.lock.acquire()
        self.value = self.value + 1
        self.lock.release()

def worker(c):
    for i in range(2):
        pause = random.random()
        print("sleeping {0}".format(pause))
        time.sleep(pause)
        c.incre
