import signal
# Test signal.setitimer() function
signal.setitimer(signal.ITIMER_REAL, 1, 1)
print("Timer started!")

def signal_handler(signum, frame):
    print("\nReceive a signal, interrupt!")
    sys.exit(0)

signal.signal(signal.SIGALRM, signal_handler)

while True:
    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        print("Keyboard interrupt!")
        sys.exit(0)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
