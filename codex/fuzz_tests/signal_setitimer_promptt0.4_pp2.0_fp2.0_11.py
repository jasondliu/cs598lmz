import signal
# Test signal.setitimer()
def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL,0.1)
# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.setitimer(signal.ITIMER_REAL,0)
# Now do some work with the open port

# Set the timeout
old_handler = signal.signal(signal.SIGALRM, handler)
signal.alarm(5)
try:
    print('Connecting to the server...')
    response = urllib.urlopen('http://www.google.com', timeout=10)
    html = response.read()
    print(html)
except Exception, err:
    print("Exception: {0}".format(err))
finally:
    signal.signal(
