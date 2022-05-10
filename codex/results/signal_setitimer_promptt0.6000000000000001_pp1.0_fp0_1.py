import signal
# Test signal.setitimer()
#
# This test is supposed to be run in an environment where itimer virtual
# time is switched off (e.g. setitimer(ITIMER_VIRTUAL) is not supported).
#
# The test checks that the signal handler is called on time even if the
# process is executing a sleep() call.
#
# Usage: ./itimer.py

def handler(sig, frame):
    print("Caught signal: %d" % sig)

signal.signal(signal.SIGALRM, handler)

# signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0, 0.1)

print("Before sleep")
signal.pause()
print("After sleep")

#time.sleep(0.5)
#time.sleep(0.1)
time.sleep(2)

print("Done")
