import threading
# Test threading daemon

def work(cnt):
    print(cnt)
    time.sleep(cnt)

t = threading.Thread(target=work, args=(3, ))
t.setDaemon(True)
t.start()

print('end')

# Test threading lock

class ShareData(threading.Thread):
    def __init__(self, cnt, lock):
        super().__init__()
        self.cnt = cnt
        self.lock = lock
    def run(self):
        self.lock.acquire()
        for i in range(self.cnt):
            print(i)
        self.lock.release()

lock = threading.Lock()

th1 = ShareData(5, lock)
th2 = ShareData(5, lock)

th1.start()
th2.start()

# Test threading RLock

class ShareData(threading.Thread):
    def __init__(self, cnt, lock):
        super().__init__()
        self.cnt = cnt

