import signal
# Test signal.setitimer()

import sys

if sys.platform.startswith('linux'):
    # Linux only support ITIMER_VIRTUAL and ITIMER_PROF
    SIGNALS = [signal.SIGVTALRM, signal.SIGPROF]
else:
    SIGNALS = [signal.SIGALRM]


def handler(signum, frame):
    print('Got signal:', signum)


for sig in SIGNALS:
    signal.signal(sig, handler)


def test_signal(sig, timer):
    signal.setitimer(timer, 1.0, 0.5)
    print('Sleeping for 4 seconds')
    time.sleep(4)
    print('Done')


for timer in SIGNALS:
    test_signal(timer, timer)
