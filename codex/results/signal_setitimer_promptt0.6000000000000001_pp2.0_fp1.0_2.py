import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Call handler() in 2 seconds
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 2)

# Do some work, and check the timer every so often
count = 0
while True:
    print 'Working...'
    time.sleep(0.5)
    count += 1
    if count > 5:
        print 'Exiting'
        break
