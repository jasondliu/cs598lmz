import signal
# Test signal.setitimer() with SIGTSTP.

def handler(signum, frame):
    if signum == signal.SIGALRM:
        print('Got SIGALRM')
    elif signum == signal.SIGTSTP:
        print('Got SIGTSTP')

signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGTSTP, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    signal.pause()
