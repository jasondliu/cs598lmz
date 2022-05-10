import signal
# Test signal.setitimer() and signal.getitimer()

# This test is not useful on Windows.
if sys.platform == "win32":
    exit(0)

seconds = 1.0

def handler(signum, frame):
    print("Handler called for signal", signum)
    raise SystemExit(4)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, seconds, seconds)

start = time.time()
try:
    while 1:
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.1)
except SystemExit as e:
    end = time.time()
    period = end - start
    print("\nTest took {} seconds".format(period))
    if period < 2.0 or period > 3.0:
        print("FAILED")
        exit(1)
    else:
        print("OK")
        exit(e.code)
