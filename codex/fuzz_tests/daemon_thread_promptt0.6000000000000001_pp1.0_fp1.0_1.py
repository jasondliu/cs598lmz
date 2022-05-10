import threading
# Test threading daemon
class MyThread(threading.Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name
    def run(self):
        global num
        time.sleep(1)
        num += 1
        # print('%s\n' %(threading.current_thread()))
        print('%s set num to %d' % (self.name, num))

num = 0
t1 = MyThread('t1')
t2 = MyThread('t2')
t1.start()
t2.start()
t1.join()
t2.join()
print('main thread stop! num is %d\n' %(num))

# Test threading Lock
num = 0
lock = threading.Lock()
def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_num(n)
        finally:
            lock.release()

def change_num(n):
    global num
    num += n
