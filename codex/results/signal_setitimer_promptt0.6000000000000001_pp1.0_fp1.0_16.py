import signal
# Test signal.setitimer
def alarm_handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")
signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL,0.1)
# This open() may hang indefinitely
mf = open('/dev/mtdblock0')

# Test signal.set_wakeup_fd
signal.set_wakeup_fd(mf.fileno())
print('About to sleep')
signal.pause()
