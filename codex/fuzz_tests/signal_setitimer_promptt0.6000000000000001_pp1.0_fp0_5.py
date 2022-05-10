import signal
# Test signal.setitimer

import signal

def handler(signum, frame):
    print "handler"

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 1)

while True:
    continue

# handler
# handler
# handler
# handler
# handler
# handler
# handler
# handler
# handler
# handler
# handler
# ^CTraceback (most recent call last):
#   File "setitimer.py", line 13, in <module>
#     continue
# KeyboardInterrupt
#
# Process finished with exit code 1
