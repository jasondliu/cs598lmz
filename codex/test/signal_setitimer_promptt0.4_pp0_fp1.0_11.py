import signal
# Test signal.setitimer()
#
# This script will send a SIGALRM after 1 second and then exit
#
# You can test this by running in one terminal:
#   $ python3 test_setitimer.py
# and in another:
#   $ while true; do kill -l; sleep 1; done
#
# You should see the signal number 14 (SIGALRM) appear in the second
# terminal.

def handler(signum, frame):
    print("Got signal", signum)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

while True:
    pass
