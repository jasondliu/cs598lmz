import threading
# Test threading daemonic
class ThreadClass(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = 'I am ' + self.name + ' @ ' + str(i)
            print(msg)

# main
for i in range(5):
    t = ThreadClass()
    #t.setDaemon(True)
    t.start()

main_thread = threading.current_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    t.join()

print('Main thread exit.')

# Test threading lock
class Counter(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start
    def increment(self):
        self.lock.acquire()
        try:
            self.value = self.value + 1
        finally:
            self.lock.release()

class Worker(threading.Thread):
    def __init__(self, counter
