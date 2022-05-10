import signal
# Test signal.setitimer with timerid=ITIMER_REAL, interval=0.01, interation=200
# interval of the timer will be updated
test_iteration = 200
interval = 0.01
signal.signal(signal.SIGALRM, lambda x,y: None)
signal.setitimer(signal.ITIMER_REAL, interval, interval)
for i in range(test_iteration):
    signal.setitimer(signal.ITIMER_REAL, i/100, i/100)
    try:
        signal.pause()
    except Exception as e:
        print('Alarm signal interruted: {}'.format(e))
        sys.exit(1)
