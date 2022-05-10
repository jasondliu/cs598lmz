import signal
# Test signal.setitimer()


def handler(signum, frame):
    print("Alarm handler called")
    raise IOError("I/O operation timed out")


signal.signal(signal.SIGALRM, handler)

for i in range(3):
    print("Setting alarm for %d seconds..." % i)
    signal.setitimer(signal.ITIMER_VIRTUAL, i)
    try:
        print("Doing I/O operation that may block")
        f = open("/")  # open the root directory for reading
    except IOError:
        print("I/O operation timed out")
    else:
        print("I/O operation succeeded!")
        f.close()

print("Done")
