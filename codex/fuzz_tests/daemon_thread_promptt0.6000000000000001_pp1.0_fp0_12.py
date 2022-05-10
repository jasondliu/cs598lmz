import threading
# Test threading daemon
class MyThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.t_name = name
        self.is_daemon = True
    def run(self):
        print 'Thread %s is running...' % self.t_name
        print 'Thread %s is ended.' % self.t_name
t = MyThread('daemon_thread')
t.start()
