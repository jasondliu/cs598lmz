import threading
# Test threading daemon
# https://stackoverflow.com/questions/3788208/python-threading-filter-by-attribute

class MyThread(threading.Thread):
    def __init__(self, number, style):
        threading.Thread.__init__(self)
        self.number = number
        self.style = style

    def run(self):
        print 'Thread %s started' % self.number
        time.sleep(1)
        print 'Thread %s finished' % self.number

for i in range(10):
    t = MyThread(i, 'daemon' if i % 2 else 'normal')
    if t.style == 'daemon':
        t.setDaemon(True)
    t.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    print t.getName()
    if t.style == 'daemon':
        t.join()

print 'Main thread exit'

# Test threading lock
# https://stack
