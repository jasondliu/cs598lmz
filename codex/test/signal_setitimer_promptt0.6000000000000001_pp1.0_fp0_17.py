import signal
# Test signal.setitimer()
def alarm_handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL,0.1)

try:
    f = open('/dev/ttyS0','r')
    print(f.read())
    f.close()
except OSError as err:
    print('OS error: {0}'.format(err))

signal.alarm(0)
print('done')
# Test signal.setitimer()
def alarm_handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL,0.1)

