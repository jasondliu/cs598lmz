import signal
# Test signal.setitimer()

import time

def handler(signum, frame):
    print("Signal handler called with signal", signum)

signal.signal(signal.SIGALRM, handler)

def main():
    print("Setting the alarm")
    signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
    print("Sleeping")
    time.sleep(10)
    print("Done")

main()
