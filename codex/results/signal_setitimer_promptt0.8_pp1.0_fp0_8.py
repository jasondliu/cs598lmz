import signal
# Test signal.setitimer() and signal.getitimer()
# First, define the signal handler

def printit(sig, frm):
    print("Got signal : ",sig);
    print("Time Remaining: ",signal.getitimer(signal.ITIMER_PROF));
    signal.setitimer(signal.ITIMER_PROF,0.0);
    print("Time Remaining: ",signal.getitimer(signal.ITIMER_PROF));
# Now set the SIGPROF handler and set an alarm
signal.signal(signal.SIGPROF, printit);
signal.setitimer(signal.ITIMER_PROF, 0.5);
# Now do some work while the alarm is ticking
time.sleep(0.1);
i = 0
while i<0xFFFFFFFF:
    i=i+1;
# printit() should have been called twice by now
#
#------------------------------------------------------------------------------
