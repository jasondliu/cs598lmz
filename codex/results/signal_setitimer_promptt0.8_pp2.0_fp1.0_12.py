import signal
# Test signal.setitimer() with ITIMER_REAL

def sig_alarm(signum, frame):
    print('SIGALRM received')

signal.signal(signal.SIGALRM, sig_alarm)
itimer = signal.getitimer(signal.ITIMER_REAL)
try:
    signal.setitimer(signal.ITIMER_REAL, 1)
    while 1:
        print('still here')
        time.sleep(2)
except KeyboardInterrupt:
    pass
print(signal.getitimer(signal.ITIMER_REAL))
signal.setitimer(signal.ITIMER_REAL, itimer)

# Test signal.setitimer() with ITIMER_VIRTUAL

def sig_vtalrm(signum, frame):
    print('SIGVTALRM received')

signal.signal(signal.SIGVTALRM, sig_vtalrm)
itimer = signal.getitimer(signal.ITIMER_VIRTUAL)
try:

