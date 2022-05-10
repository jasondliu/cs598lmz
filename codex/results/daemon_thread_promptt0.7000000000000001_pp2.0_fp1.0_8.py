import threading
# Test threading daemon
# http://stackoverflow.com/questions/3036558/making-a-python-daemon-thread


class MyThread(threading.Thread):
    def run(self):
        print "Starting"
        time.sleep(10)
        print "Exiting"

for i in range(3):
    t = MyThread()
    t.setDaemon(True)
    t.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    print "joining %s" % t.getName()
    t.join()

print "Finished"

# Test threading lock
# http://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread

class Thread1(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        threading.Thread.__init
