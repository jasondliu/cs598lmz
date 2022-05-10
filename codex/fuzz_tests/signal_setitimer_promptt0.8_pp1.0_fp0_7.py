import signal
# Test signal.setitimer() with a signal that is not specified in
# the signal module (SIGPOLL).  (For platforms where SIGPOLL is
# defined.)

signal.signal(signal.SIGPOLL, signal.SIG_IGN)
signal.setitimer(signal.ITIMER_REAL, 1.0, 0)
expected_message = "signal.setitimer: signal SIGPOLL not defined"

try:
    signal.setitimer(signal.ITIMER_REAL, 1.0, 0)
except RuntimeError as exc:
    assert exc.args[0] == expected_message
else:
    raise TestFailed('setitimer(signal.ITIMER_REAL, 1.0, 0) did not '
                     'raise RuntimeError')

try:
    signal.setitimer(signal.ITIMER_VIRTUAL, 1.0, 0)
except RuntimeError as exc:
    assert exc.args[0] == expected_message
else:
    raise TestFailed('setitimer(signal.ITIM
