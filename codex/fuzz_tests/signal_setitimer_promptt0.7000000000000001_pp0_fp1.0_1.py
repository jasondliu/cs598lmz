import signal
# Test signal.setitimer to send SIGALRM to the caller
# and how Python responds to it.

def alrm_handler(sig, frame):
    print "got SIGALRM"

signal.signal(signal.SIGALRM, alrm_handler)

print "setting itimer..."
signal.setitimer(signal.ITIMER_REAL, 2, 0)

print "sleeping ..."
time.sleep(5)

print "done"
