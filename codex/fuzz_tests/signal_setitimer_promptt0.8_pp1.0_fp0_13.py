import signal
# Test signal.setitimer() for a different period of time
def alarm_handler(signum, frame):
    "handler"
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL,5,0)

# This open() may hang indefinitely
# f = open('/dev/ttyS0', 'r')

# After 10 seconds, a SIGALRM signal is sent
# Our signal handler is called, and the file is closed

# while 1:
#     print "*"
#     pass

# f.close()

# #print "Done"


import pdb; pdb.set_trace() # debugging starts here

signal.alarm(0)           # Disable the alarm
signal.alarm(10)  # Enable the alarm again

print('Finis')
