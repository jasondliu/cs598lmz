import signal
# Test signal.setitimer
# Set an alarm for 2 seconds and catch it

def handler(signum, frame):
    print 'Signal handler called with signal', signum


# Call handler on SIGALRM
signal.signal(signal.SIGALRM, handler)

# Set an alarm for 2 seconds
signal.setitimer(signal.ITIMER_REAL, 2)


# Do some work
count = 0
while True:
    try:
        count += 1
        print count
    except KeyboardInterrupt:
        break
