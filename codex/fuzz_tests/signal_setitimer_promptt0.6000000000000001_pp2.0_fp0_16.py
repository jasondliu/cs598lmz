import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)
    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

print("Continuing")

# Signal handlers are inherited by forked processes
pid = os.fork()
if pid == 0:
    print('Child:', os.getpid())
    os.close(fd)
    time.sleep(100)
else:
    print('Parent:', os.getpid())
    os.waitpid(pid, 0)

print("Done")
