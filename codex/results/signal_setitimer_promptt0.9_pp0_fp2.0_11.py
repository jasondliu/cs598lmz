import signal
# Test signal.setitimer [not in use]
signal.signal(signal.SIGALRM, lambda signum, stack_frame: None)
signal.setitimer(signal.ITIMER_REAL, 1, 1)
print('This line will never run')
'''

import time
import threading

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
        with self._cv
