import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 3\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 4\n')).start()

"""

import sys
from threading import Thread

class OutputWriter(Thread):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def run(self):
        sys.stdout.write(self.text + '\n')

threads = [OutputWriter('Hello from thread {}'.format(i)) for i in range(4)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

"""

import sys
from threading import Thread

