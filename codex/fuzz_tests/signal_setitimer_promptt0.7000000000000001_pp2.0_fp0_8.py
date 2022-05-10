import signal
# Test signal.setitimer

def alarm(signum, frame):
    raise TimeoutError

signal.signal(signal.SIGALRM, alarm)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
try:
    while True:
        pass
except TimeoutError:
    print('Time is out')
'''

from threading import Timer
from time import sleep


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.next_call = time.time()
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self.
