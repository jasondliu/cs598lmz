import threading
# Test threading daemon
# https://stackoverflow.com/questions/19071512/python-threading-daemon-vs-none

import time
import random

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.daemon = True

    def run(self):
        while True:
            time.sleep(random.randint(1,5))
            print(self.name)

for i in range(5):
    t = MyThread(str(i))
    t.start()

time.sleep(10)
print('Main thread exiting.')

# Main thread exiting.
# 0
# 1
# 2
# 3
# 4
# 0
# 1
# 2
# 3
# 4
# 0
# 1
# 2
# 3
# 4
# 0
# 1
# 2
# 3
# 4
# 0
# 1
# 2
# 3
# 4
# 0
# 1
# 2
#
