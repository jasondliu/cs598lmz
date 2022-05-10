import signal
# Test signal.setitimer(2,3,4)
try:
    signal.setitimer(2, 3, 4)
except TypeError:
    print('TypeError')

print('[setitimer]')
th=time.monotonic()
signal.setitimer(signal.ITIMER_REAL, 1, 1)
while time.monotonic()-th<3:
    time.sleep(0.2)
    print(time.monotonic())
signal.setitimer(signal.ITIMER_REAL, 0, 0)

print('[alarm]')
th=time.monotonic()
signal.alarm(1)
while time.monotonic()-th<2.5:
    time.sleep(0.2)
    print(time.monotonic())
signal.alarm(0)

print('[pause]')
signal.pause()

print('[siginterrupt]')
signal.siginterrupt(signal.SIGALRM, False)
signal.alarm(1)
