import signal
# Test signal.setitimer()
# set the timer to 5 seconds, the call the alarm handler after 5 seconds
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL,5)

for i in xrange(5):
    print "sleep 3 sec"
    time.sleep(3)

print "end"



''' 
Reference:
1. https://docs.python.org/2/library/signal.html

'''
