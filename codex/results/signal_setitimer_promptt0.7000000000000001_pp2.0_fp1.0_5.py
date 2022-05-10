import signal
# Test signal.setitimer()
def a(signum,frame):
    print "here"
    print signum
    print frame
signal.alarm(1)
signal.setitimer(signal.ITIMER_VIRTUAL,3,3)
signal.signal(signal.ITIMER_VIRTUAL,a)
while True:
    print "still alive"
