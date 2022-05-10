import signal
# Test signal.setitimer() and signal.alarm()

import test.support

signal.setitimer(signal.ITIMER_REAL, 0.3, 1)
signal.alarm(1)

try:
    # wait for SIGALRM
    signal.pause()
    print("pause() returned")
    test.support.exit(1)
except OSError:
    # Irix and OSF/1 raise OS exceptions instead of returning
    print("pause() raised OSError", sys.exc_info()[1])
    test.support.exit(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt")
    test.support.exit(1)

print("pause() returned, good")
signal.setitimer(signal.ITIMER_REAL, 0, 0)
signal.alarm(0)
test.support.exit(0)
