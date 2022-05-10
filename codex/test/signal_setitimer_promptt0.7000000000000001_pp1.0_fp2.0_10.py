import signal
# Test signal.setitimer for ITIMER_PROF.

# This test needs to be run with root permission, since it changes the
# process's signal handler.

# Create a file with a size of 4 MB.
f = open('test.dat', 'w')
for i in range(0, 4 * 1024 * 1024):
    f.write(' ' * 1024)
f.close()

# Specify the signal handler.
def handler(signum, frame):
    print('receive signal %d' % signum)

# Register signal handler.
signal.signal(signal.SIGPROF, handler)

# Run 5 seconds.
signal.setitimer(signal.ITIMER_PROF, 1, 0)
time.sleep(5)
