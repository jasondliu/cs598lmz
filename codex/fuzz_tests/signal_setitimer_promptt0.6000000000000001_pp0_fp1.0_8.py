import signal
# Test signal.setitimer()

def handler(num, frame):
    print('Alarm :', time.ctime())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5, 0)
while True:
    signal.pause()
