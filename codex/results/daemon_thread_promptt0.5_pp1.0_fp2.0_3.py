import threading
# Test threading daemon
class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        global num
        time.sleep(1)
        # lock.acquire()
        num += 1
        # lock.release()
        print('%s set num to %s' % (self.name, num))

num = 0
# lock = threading.Lock()
thread_list = []
for i in range(100):
    t = MyThread(str(i))
    t.setDaemon(True)
    thread_list.append(t)

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()

print('exit main thread')
