import signal
# Test signal.setitimer(signal.ITIMER_PROF, x, y)
# where x > y
# Expected behaviour: signals are not generated
signal_count = 0
def handler(signum, frame):
    global signal_count
    signal_count += 1

signal.signal(signal.SIGPROF, handler)
signal.setitimer(signal.ITIMER_PROF, 1.0, 0.0)

# give time for timer to expire
a = signal_count
while signal_count == a:
    pass

assert signal_count > a

# a > b, so no signals should be sent
signal.setitimer(signal.ITIMER_PROF, 2.0, 1.0)
assert signal_count > a

print("Done")
