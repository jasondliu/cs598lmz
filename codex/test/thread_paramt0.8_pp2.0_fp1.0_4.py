import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread\n')).start()
 
import threading, time

class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        '''
        Run the timer and notify waiting threads after each interval
        '''
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def wait_for_tick(self):
        '''
        Wait for the next tick of the timer
        '''
