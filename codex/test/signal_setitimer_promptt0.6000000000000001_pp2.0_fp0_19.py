import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(1)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(1)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(1)
print('Done')
# Test signal.signal
def handler(signum, frame):
    print('Received signal', signum)
signal.signal(signal.SIGALRM, handler)
signal.alarm(1)
time.sleep(1)
signal.alarm(1)
time.sleep(1)
signal.alarm(1)
time.sleep(1)
print('Done')
# Test signal.getsignal
print(signal.getsignal(signal.SIGALRM))
print(signal.getsignal(signal.SIGINT))
# Test signal.signal
