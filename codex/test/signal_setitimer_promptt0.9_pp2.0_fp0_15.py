import signal
# Test signal.setitimer() on Linux and macOS

# Does not works on macOS X but does on Linux
# Also seems to work on Windows

# setitimer() takes 3 arguments
# 1st arg: ITIMER_VIRTUAL - use it to create a per-process timer
# 2nd arg: number of seconds after which the timer should expire
# 3rd arg: interval in seconds after which the subsequent timer should expire
signal.setitimer(signal.ITIMER_VIRTUAL, 3, 0)

# Register setitimer() handler which should run after the timer expires
signal.signal(signal.SIGVTALRM, handler)

while True:
    print(".", end="")  # Keep the while loop running

