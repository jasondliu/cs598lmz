import signal
# Test signal.setitimer() and signal.getitimer()
# some code snippets taken from The Python Library Reference, Release 2.6.4,
# first section of 14.1.2.
# Signal handler for SIGALRM; must be defined before setitimer call so that
# it won't get optimized away. Value will be set to 1 by signal handler.
#global alarm_fired

alarm_fired = False
def alarmHandler(signum, frame):
    global alarm_fired
    alarm_fired = True
    
signal.signal(signal.SIGALRM, alarmHandler)

# interval = 0.1
# Set an alarm
#signal.setitimer(0.1)

#while not alarm_fired:
#    print "not yet"
    
# Stop the alarm
##signal.setitimer(0)
#print "done"

def signalhandler(signum, frame):
    print "Frame", frame
    print "Signum", signum
    
def checkSignal(signum):
    try:
        signal.signal(signum, signalhandler)

