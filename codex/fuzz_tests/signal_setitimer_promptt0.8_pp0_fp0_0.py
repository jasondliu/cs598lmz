import signal
# Test signal.setitimer function. 

# This is a bit tricky, as we're going to set an alarm, and then
# we're going to set an alarm within that alarm.  The result should 
# be that the inner alarm gets called first, but we should still
# get the outer alarm too. 

alarms = 0 

def handler(signum, frame):
    global alarms
    alarms += 1 
    if alarms == 1:
        print("Hello!")
        signal.setitimer(signal.ITIMER_REAL, 0.1)
    else:
        print("Goodbye!")
        quit()
        
signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 1)
print("waiting...")
