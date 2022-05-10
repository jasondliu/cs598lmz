import signal
# Test signal.setitimer to generate SIGALRM
# Test signal.signal to set the handler to SIGALRM
# Test signal.alarm to set the time to generate SIGALRM
# Test signal.getsigmask to check the current blocked signals
# Test signal.setitimer to generate SIGVTALRM
# Test signal.signal to set the handler to SIGVTALRM
# Test signal.alarm to set the time to generate SIGVTALRM
# Test signal.getsigmask to check the current blocked signals
# Test signal.setitimer to generate SIGPROF
# Test signal.signal to set the handler to SIGPROF
# Test signal.alarm to set the time to generate SIGPROF
# Test signal.getsigmask to check the current blocked signals

# These values are set on the command line

signal_num = signal_name = None

# These global variables will be used to keep track of the test results

result_dict = {}

# This is a list of the SIGPROF, SIGALRM and SIGVTALRM signals.
# It is used to determine when all the timers have expired.

signal
