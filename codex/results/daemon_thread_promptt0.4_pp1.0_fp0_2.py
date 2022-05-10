import threading
# Test threading daemon
from time import sleep
from random import randint
from datetime import datetime

class ThreadingDaemon(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.daemon = True
        self.start()

    def run(self):
        while True:
            print(self.name, ':', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            sleep(randint(1, 10))

threading_daemon = ThreadingDaemon('ThreadingDaemon')
print('Main thread sleep for 20 seconds')
sleep(20)
print('Main thread exit')
