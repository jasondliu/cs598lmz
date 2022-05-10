import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread-1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread-2\n')).start()

# 同步
import sys, threading

class StdOutListener(threading.Thread):
    def __init__(self, prefix):
        threading.Thread.__init__(self)
        self.prefix = prefix

    def run(self):
        sys.stdout.write(self.prefix)

threads = [StdOutListener('Thread-1\n'), StdOutListener('Thread-2\n')]
for t in threads:
    t.start()
for t in threads:
    t.join()

# 同步
import sys, threading, time

class StdOutListener(threading.Thread):
    def __init__(self, prefix):
        threading.Thread.__init__(self)
        self.prefix = prefix

    def run(self):
        sys.stdout.write(self.prefix)
       
