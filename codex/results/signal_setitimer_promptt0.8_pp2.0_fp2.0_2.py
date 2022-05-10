import signal
# Test signal.setitimer() and signal.getitimer()
# Set interval timer to 3 sec and 0 microseconds
# Then sleep for 1 second to set off timer.
# Catch SIGALRM and print msg then exit.
def sig_handler(signo, sig_stack):
    print("Caught signal ", signo,", stack frame is", sig_stack)
    # Restore the previous alarm settings.
    signal.setitimer(signal.ITIMER_REAL, 0)
    sys.exit(0)

# Set the signal handler
signal.signal(signal.SIGALRM, sig_handler)

# Set an alarm for 3 seconds
signal.setitimer(signal.ITIMER_REAL, 3, 0)

# Wait for the signal
time.sleep(5)

# If we reach here, no signal was delivered
print("No signal was delivered!")

# Set interval timer to 3 sec and 0 microseconds
# Then sleep for 1 second to set off timer.
# Catch SIGALRM and print msg then exit.
def sig_handler(signo, sig_stack):
