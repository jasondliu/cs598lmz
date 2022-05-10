import threading
# Test threading daemon mode
# After parent thread terminated, child threads will be terminated too
class ThreadTest(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self, *args, **kwargs):
        for i in range(10):
            print '%s: %d' % (threading.currentThread(), i)
            time.sleep(1)


if __name__ == '__main__':
    thread_list = []
    for i in range(5):
        t = ThreadTest()
        thread_list.append(t)
        t.start()

    for i in range(5):
        print '%s: %d' % (threading.currentThread(), i)
        time.sleep(1)
    print 'Main thread end.'
