import signal
# Test signal.setitimer
def handler(signum, frame):
    print "Timer expired, waking up..."
    # Restore to original handler
#    signal.signal(signum,signal.SIG_DFL)
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.01)
print "Blocking"
for i in range(1000000):
     print ".",
# The signal will be received
# when system timer is up
time.sleep(3)
