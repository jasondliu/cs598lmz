import signal
# Test signal.setitimer()
import unittest
from test.support import reap_children

# See test_time for more tests of the system-specific functions.

def check_alarm(time, expected):
    caught = []
    timeout = []
    def on_alarm(signum, frame):
        caught.append(signum)
        timeout.append(time)
    def alarm_handler():
        signal.signal(signal.SIGALRM, on_alarm)
        signal.setitimer(signal.ITIMER_REAL, time)
        time.sleep(0.01)
    t = threading.Thread(target=alarm_handler)
    t.start()
    t.join()
    if timeout:
        real_time = timeout[0] - time.time()
        if real_time > expected * 1.1:
            raise unittest.SkipTest(
                    'SIGALRM is broken on this platform')
    else:
        # The on_alarm handler may be called later, in which case the
        # check below would fail. 
