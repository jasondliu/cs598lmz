import signal
# Test signal.setitimer()
#
# PythonDocs has:
#     signum: Signal number, such as signal.SIGINT; see the signal module.
#     value: The time until the timer will fire: a (seconds, microseconds)
#            tuple, or 0 to cancel the timer.
#     ovalue: Previous value of the timer: a (seconds, microseconds) tuple, or
#             None if the timer has never been set.
#
# The limit to the time interval on UNIX is:
#   CONST_HZ <= interval*1e6 <= CONST_HZ*2**31-1
#   where CONST_HZ is a 60-bit constant. This is at least 100 years.

# Tries to set the timeitimer and reports via the handler.
# We use the standard signal names (SIGALRM and SIGVTALRM)
# to prevent conflict with other signal names.
def setitimer(sigtype, interval):
   signal.signal(sigtype, handler)
   signal.setitimer(sigtype, interval, interval)
   signal.pause()

