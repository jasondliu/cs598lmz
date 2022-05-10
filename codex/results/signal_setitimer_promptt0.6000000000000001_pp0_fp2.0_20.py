import signal
# Test signal.setitimer()

# first we need a way of detecting when a signal has been delivered

# This is set to True by our signal handler
signal_received = False
# This is set to the signal number received
sig_num = None

# This is our signal handler
def signal_handler(sig_num, stack_frame):
    global signal_received, sig_num
    signal_received = True
    sig_num = sig_num

# We install our signal handler
signal.signal(signal.SIGALRM, signal_handler)

# We set the timer for 2 seconds
signal.setitimer(signal.ITIMER_REAL, 2, 0)

# We wait for the signal to be delivered
while not signal_received:
    pass

# We print out the signal number
print("Signal %i received" % sig_num)

# We set the timer for 2 seconds
signal.setitimer(signal.ITIMER_REAL, 2, 0)

# We wait for the signal to be delivered
while not signal_received:

