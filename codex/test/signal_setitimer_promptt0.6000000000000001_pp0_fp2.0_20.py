import signal
# Test signal.setitimer()

# first we need a way of detecting when a signal has been delivered

# This is set to True by our signal handler
signal_received = False
# This is set to the signal number received
sig_num = None

# This is our signal handler
