import signal
# Test signal.setitimer function

def handler(signum, frame):
    print("Got alarm", signum)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
start = datetime.datetime.now()
while True:
    now = datetime.datetime.now()
    delta = (now - start).total_seconds()
    if delta > 0.5:
        break
    print("wait")
    time.sleep(0.2)
signal.setitimer(signal.ITIMER_REAL, 0, 0)

print("done")

# TTY test

import sys
from tty import setcbreak

tty_fd = sys.stdin.fileno()
setcbreak(tty_fd)
while True:
    c = sys.stdin.read(1)
    if c == "q":
        break
    print("Got {}".format(c))

# vim: sw=4 ts=4 et
