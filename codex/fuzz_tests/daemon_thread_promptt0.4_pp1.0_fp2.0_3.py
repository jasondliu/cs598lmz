import threading
# Test threading daemon
# https://docs.python.org/3/library/threading.html#thread-objects
class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        global g_counter
        while True:
            print('thread {0} is running'.format(self.name))
            time.sleep(1)
            g_counter += 1
            if g_counter > 10:
                break

if __name__ == '__main__':
    g_counter = 0
    t1 = MyThread('t1')
    t2 = MyThread('t2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
