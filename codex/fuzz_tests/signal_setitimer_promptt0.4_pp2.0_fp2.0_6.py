import signal
# Test signal.setitimer()
#
# $Id: setitimer.py,v 1.1 2004/07/05 09:27:32 bskaja Exp $

def handler(signum, frame):
    print 'handler:', signum

signal.signal(signal.SIGALRM, handler)

# Set the timer to go off in 1 second
signal.setitimer(signal.ITIMER_REAL, 1, 0)
print 'sleep(2)'
time.sleep(2)

# Set the timer to go off in 1 second and repeat every 2 seconds
signal.setitimer(signal.ITIMER_REAL, 1, 2)
print 'sleep(3)'
time.sleep(3)

# Turn off the timer
signal.setitimer(signal.ITIMER_REAL, 0, 0)
print 'sleep(2)'
time.sleep(2)

# Set the timer to go off in 1 second
signal.setitimer(signal.ITIMER_REAL, 1, 0)
print 'sleep(2)'

