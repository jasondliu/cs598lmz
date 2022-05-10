import threading
# Test threading daemon
class MyThread(threading.Thread):
    def __init__(self, number, style, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self.number = number
        self.style = style
    def run(self):
        print 'thread %s number %s' %(self.name, self.number)
        if self.style == 'Daemon':
            time.sleep(1)
        print 'thread {0} done'.format(self.name)

if __name__ == '__main__':
    for i in range(10):
        t = MyThread(i, 'Daemon')
        t.setDaemon(True)
        t.start()
    time.sleep(2)
    print 'Main thread exit'
