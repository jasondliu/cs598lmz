import threading
# Test threading daemon
class ThreadTest(threading.Thread):
    def run(self):
        print('thread %s is running....' % threading.current_thread().name)
        n = 0
        while n < 5:
            n += 1
            print('thread %s >>> %s' % (threading.current_thread().name, n))
            time.sleep(1)
        print('thread %s ended.' % threading.current_thread().name)
        
# Test threading lock
lock = threading.Lock()
class ThreadTest2(threading.Thread):
    _balance = 0
    def run(self):
        while self._balance < 5:
            with lock:
                self._balance += 1 
                print('thread %s add one balance, now balance is %s' % (threading.current_thread().name, self._balance))
        print('thread %s ended.' % threading.current_thread().name)
    
    
if __name__ == '__main__':
    print('thread %s is running...' % threading.current_thread().name)

