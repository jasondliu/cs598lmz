import signal
# Test signal.setitimer()
#
# This test will run for about 10 seconds, then exit with a return code of
# zero.  If it exits with a non-zero return code, or if it crashes, then
# there is a problem with the signal.setitimer() function.

def handler(signum, frame):
    print("handler called")
    raise SystemExit

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

# The following loop will run for about 10 seconds, then the SIGALRM
# signal will be raised, calling the handler() function above.

for i in range(100):
    print(i)
    time.sleep(0.1)
