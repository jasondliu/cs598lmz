import signal
# Test signal.setitimer
def sig_alrm(signum, frame):
    print('SIGALRM received')
signal.signal(signal.SIGALRM, sig_alrm)
signal.setitimer(signal.ITIMER_REAL, 1, 5)
print('frist start')
signal.pause()
print('sleep 3 seconds')
time.sleep(3)
signal.setitimer(signal.ITIMER_REAL, 1, 5)
print('second start')
sig
