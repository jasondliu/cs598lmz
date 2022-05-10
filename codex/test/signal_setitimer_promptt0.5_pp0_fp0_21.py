import signal
# Test signal.setitimer()
def handler(signum, frame):
    print('Alarm :', time.ctime())
    signal.setitimer(signal.ITIMER_REAL, 2)
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 2)

while True:
    time.sleep(1)
