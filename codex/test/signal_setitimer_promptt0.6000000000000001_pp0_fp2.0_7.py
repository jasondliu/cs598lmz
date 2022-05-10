import signal
# Test signal.setitimer()

def signal_handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("'setitimer' causes exception")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/pts/2', os.O_RDWR)

os.write(fd, b'Hello world\n')
os.close(fd)

print('Sleeping')
time.sleep(10)
print('Exiting')
