import signal
# Test signal.setitimer()


def alarmhandler(signum, frame):
    print('alarm!')


signal.signal(signal.SIGALRM, alarmhandler)

signal.setitimer(signal.ITIMER_REAL, 5)
print('sleeping...')
time.sleep(10)
print('done')
