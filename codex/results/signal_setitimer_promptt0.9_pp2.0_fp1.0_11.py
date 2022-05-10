import signal
# Test signal.setitimer()

from test_support import verbose, TestFailed

if verbose:
    print 'SIGALRM signal handler called'
    frames = []
    for frame in sys._current_frames().itervalues():
        frames.append(frame.f_code.co_filename + 
                      ':' + str(frame.f_lineno))
    print '\n'.join(frames)

def alarm_received(signum, frame):
    raise TestFailed, "alarm_received is not supposed to be called"

signal.signal(signal.SIGALRM, alarm_received)
signal.setitimer(signal.ITIMER_REAL, 1.0)
time.sleep(10.0)
