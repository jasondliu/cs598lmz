import signal
# Test signal.setitimer()

def alarm_handler(signum, frame):
    print 'Got alarm'
    signal.setitimer(signal.ITIMER_VIRTUAL, 2)

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_VIRTUAL, 2)

for i in range(5):
    print 'Sleeping'
    time.sleep(1)

print 'Done'
