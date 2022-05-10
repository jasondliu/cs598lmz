import threading
# Test threading daemon
def target():
    print('Thread started')
    time.sleep(2)
    print('Thread ended')
    
t = threading.Thread(target=target)
# t.daemon = True
t.start()

print('Main thread ended')



# Test threading lock 
lock = threading.Lock()
def func():
    print('func started')
    time.sleep(1)
    lock.release()
    print('func ended')

lock.acquire()
func()
lock.acquire()


# Test threading class
class Test(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        print('Thread %s started' %self.name)
        time.sleep(2)
        print('Thread %s ended' %self.name)

t1 = Test('1')
t2 = Test('2')

t1.start()
t2.start()

t1.join()
t2
