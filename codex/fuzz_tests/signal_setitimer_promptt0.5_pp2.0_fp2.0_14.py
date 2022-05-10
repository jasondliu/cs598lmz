import signal
# Test signal.setitimer()
#
# This test needs to be run in a separate process, as it uses
# setitimer() which will not work in the same process as the test
# driver.

# This test also needs to be run as root, as it uses RLIMIT_CPU...
if os.geteuid() != 0:
    raise RuntimeError("you need to be root")

def handler(signum, frame):
    print "handler"
    raise SystemExit

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 2)

# Set a CPU limit of 10 seconds, so the test doesn't run forever.
resource.setrlimit(resource.RLIMIT_CPU, (10, 10))

# Wait for the alarm to go off.
while True:
    pass
