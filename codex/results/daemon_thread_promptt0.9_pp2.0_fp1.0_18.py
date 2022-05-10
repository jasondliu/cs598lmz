import threading
# Test threading daemon vs non-daemon

class Counter(object):
    def __init__(self, event, count = 10):
        self.event = event
        self.count = count

    def tick(self):
        #logging.warning('Thread-%s[%s]: %s', self.name, self.daemon, self.count)
        print 'Thread-%s[%s]: %s' % (self.name, self.daemon, self.count)
        self.count -= 1
        if self.count <= 0:
            self.event.set()

    def run(self):
        while not self.event.is_set():
            self.tick()
            self.event.wait(0.5)
    
def daemon_vs_non_daemon(event):
    ticker1 = threading.Thread(target=Counter(event, 5).run, name='daemon', args=(), kwargs={'daemon': True})
    ticker2 = threading.Thread(target=Counter(event, 8).run, name='non-daemon', args=(),
