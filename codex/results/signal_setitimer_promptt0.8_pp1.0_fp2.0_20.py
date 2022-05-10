import signal
# Test signal.setitimer(), use the C version of signal.setitimer() instead
# of the Python version.
#
# start timer to send a SIGALRM in 2 seconds,
# use signal handler to increment a global variable
# once timer goes off, 
# exit if sigalrm_count is 5
#
# repeat test several times
#
# NOTE:
# it is possible that the timer has not expired yet but the interpreter is
# already exiting. It is possible to get a signal handler called after
# the interpreter is already exiting.
print "TEST signal.setitimer()"
sigalrm_count = 0

def sigalrm_handler(signum, frame):
    global sigalrm_count
    print "got signal: %d" % signum
    sigalrm_count += 1

signal.signal(signal.SIGALRM, sigalrm_handler)

for n in range(20):
    signal.setitimer(signal.ITIMER_REAL, 2, 0)
    #while sigalrm_count != 5:
    #    time.sleep(
