import signal
# Test signal.setitimer().
TIMEOUT=10
def handler(signum, frame):
    print "Signal!", signum
    #schedule.enterabs(time.time()+TIMEOUT, 1, print_timeout,argument=(TIMEOUT,))
    signal.setitimer(signal.ITIMER_REAL, TIMEOUT)
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, TIMEOUT)

# main loop
while True:
    schedule.run()
    #signal.setitimer(signal.ITIMER_REAL, TIMEOUT)
    print 123
    time.sleep(1)
