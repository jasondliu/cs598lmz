import threading
# Test threading daemon
def test_daemon():
    print('start')
    time.sleep(2)
    print('end')

if __name__ == '__main__':
    d = threading.Thread(name='daemon', target=test_daemon)
    d.setDaemon(True)
    d.start()
    d.join(1)
    print('main thread')

# Test threading lock
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁
