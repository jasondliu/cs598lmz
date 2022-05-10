import signal
# Test signal.setitimer function

from test import test_support


class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

signal.signal(signal.SIGALRM, alarm_handler)

t = test_support.TestCase( '__init__' )

lengths = [0, 1, 2, 3, 4, 5, 10, 30, 60]

for seconds in lengths:
    for microseconds in lengths:
        t.assertFails(t.assertEqual, signal.setitimer(signal.ITIMER_REAL, seconds, microseconds), None)
    for i in xrange(4):
        t.assertFails(t.assertEqual, signal.setitimer(signal.ITIMER_REAL, seconds, 0), None)
    if i%2:
        t.assertEqual(signal.signal(signal.SIGALRM, signal.SIG_IGN), alarm_handler)
        t.assertEqual(signal.setitimer(signal.ITIM
