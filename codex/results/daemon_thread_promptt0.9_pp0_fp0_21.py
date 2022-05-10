import threading
# Test threading daemon feature
# When the threading is turned into daemon, the thread is terminated forcefully.
# Time out feature is useful for such cases
class TestThread(threading.Thread):
    def __init__(self):
        self.timeout = 5
        self.result = None
        threading.Thread.__init__(self)

    def run(self):
        start = time.time()
        while not self.result and time.time()<start+self.timeout:
            try:
                self.result = urllib2.urlopen(urllib2.Request('http://www.baidu.com'))
            except Exception:
                pass
            time.sleep(0.1)
        # process results
        if self.result:
            print(self.result.read())

if __name__ == '__main__':
    t = TestThread()
    t.start()
    for i in range(10):
        time.sleep(1)
        print(i)
    if t.is_alive():
        print('Terminate thread')
        t.terminate
