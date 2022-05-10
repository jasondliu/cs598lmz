import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input("Введите ваше имя: ") + "\n")).start()
## 5
import threading
from threading import Thread
from time import sleep

class Worker(Thread):
    def __init__(self, *args, **kwargs):
        super(
            Worker,
            self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()
        self.daemon = True

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

def some_action(arg, stop):
    while not stop():
        print(arg)
        sleep(1)

def main(argv):
    stop_event = threading.Event()
    for i in range(4):
        t = Worker(target=some_action, args=(i, stop_event.is_set,))
        t.start()
    sleep(10)
    stop
