import threading
# Test threading daemon thread
class TestDaemonThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        print('%s is running...' % threading.current_thread().name)
        time.sleep(3)
        print('%s is end...' % threading.current_thread().name)


if __name__ == '__main__':
    t = TestDaemonThread('TestDaemonThread')
    t.setDaemon(True)
    t.start()
    print('%s is end...' % threading.current_thread().name)
