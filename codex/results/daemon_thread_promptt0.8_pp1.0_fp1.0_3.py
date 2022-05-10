import threading
# Test threading daemon
class MyThread(threading.Thread):
    def run(self):
        print('{} has been started!'.format(self.getName()))
        time.sleep(5)
        print('{} has been finished!'.format(self.getName()))

def test():
    for i in range(10):
        t = MyThread()
        t.start()
        t.join()
        print('{} join finished'.format(t.getName()))
    print('All join finished')

if __name__ == '__main__':
    test()
    import threadlocal
    threadlocal.test()
    import threading_lock
    threading_lock.test()
