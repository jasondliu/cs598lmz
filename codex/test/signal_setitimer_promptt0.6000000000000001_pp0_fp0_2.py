import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal:", signum)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)

try:
    while True:
        signal.pause()
except KeyboardInterrupt:
    print('end')
