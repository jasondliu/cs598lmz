import threading
# Test threading daemon
from time import sleep
import random


class Session(threading.Thread):
    def __init__(self, msg):
        threading.Thread.__init__(self)
        self.msg = msg

    def run(self):
        while True:
            print(self.msg)
            sleep(random.choice(range(1, 5)))


if __name__ == '__main__':
    for msg in ['you', 'need', 'python']:
        t = Session(msg)
        t.daemon = True
        t.start()

    print('main thread end')
