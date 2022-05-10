import signal
# Test signal.setitimer() in Python
# This should never time out
# In Python 2.3.3 you should see a SIGALRM delivered
# In Python 2.5.2 you should print "Waiting" forever

def handler(signum, frame):
    print signum, frame

for sig in [signal.SIGALRM, signal.SIGVTALRM, signal.SIGPROF]:
    signal.signal(sig, handler)
    print "Waiting for", sig
    signal.setitimer(sig, 0.5, 0.5)

    while 1:
        print ".",
        time.sleep(0.25)

print "Finished"
