import signal
# Test signal.setitimer()
def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL,0.2)

while True:
    print('Yielding')
    time.sleep(0.1)
