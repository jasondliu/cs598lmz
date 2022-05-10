import threading
# Test threading daemon

def worker():
    """thread worker function"""
    print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print "Exiting Main Thread"
# BigFileWriter

import threading
import os

class BigFileWriter(threading.Thread):
    def __init__(self, filename, *args, **kwargs):
        super(BigFileWriter, self).__init__(*args, **kwargs)
        self.filename = filename
        self.file = open(self.filename, 'a')
        self.setDaemon(True)

    def write(self, data):
        self.file.write(data)
        self.file.flush()
        os.fsync(self.file)

    def run(self):
        while True:
            line = self.queue.get()
            if line is None:
                break
            self.write(
