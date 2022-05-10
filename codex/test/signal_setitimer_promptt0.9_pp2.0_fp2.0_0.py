import signal
# Test signal.setitimer()

def send_alarm():
    print("Alarm has been sent")

# Add a signal handler for SIGALRM
signal.signal(signal.SIGALRM, send_alarm)

# This will cause SIGALRM to come in 1 second
signal.setitimer(signal.ITIMER_REAL, 1)

# Now wait for signals
signal.pause()


# Test signal.setitimer()

def send_alarm(arg1, arg2):
    print("Alarm has been sent with", arg1, arg2)

# Add a signal handler for SIGALRM
signal.signal(signal.SIGALRM, send_alarm)

# This will cause SIGALRM to come in 1 second.
# It will pass the string argument "spam" and
# the integer argument 42 to the signal handler
signal.setitimer(signal.ITIMER_REAL, 1, ("spam", 42))

# Now wait for signals
signal.pause()


