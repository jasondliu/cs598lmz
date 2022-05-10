import threading
# Test threading daemon mode
class thread_test(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
    def run(self):
        print "thread daemon mode: %s" % self.daemon
        print "thread name: %s" % threading.current_thread().name
        print "thread id: %s" % threading.currentThread().ident
        print "thread local: %s" % threading.local()
        print "thread active count: %s" % threading.active_count()
        print "thread active list: %s" % threading.enumerate()
        print "thread stack size: %s" % threading.stack_size()
        print "thread get number: %s" % threading.get_ident()
        print "thread time: %s" % time.time()
        time.sleep(100)
# Test threading
def threading_test():
    t = thread_test()
    t.start()
    print "thread daemon mode: %s" % t
