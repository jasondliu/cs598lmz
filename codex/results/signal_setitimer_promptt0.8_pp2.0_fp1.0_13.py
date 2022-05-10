import signal
# Test signal.setitimer() in Python
# See also:  http://stackoverflow.com/questions/14996453/python-libraries-to-calculate-cpu-time-and-wall-clock-time
#
# NOTE:  Does not seem to work on Cygwin.  Only works on Linux, Ubuntu.
#        Cygwin python uses the SIGALRM handler that comes with Windows.
#        Windows does not support SIGALRM, or ITIMER_REAL, or CLOCK_REALTIME.
#        See also: http://stackoverflow.com/questions/562253/how-do-i-use-sigalrm-on-windows
#
#
#
import time

# Use a signal handler to tell that timer went off
global_time = 0
def handler(signum, frame):
    global global_time
    global_time = time.time()

# Install our special handler for SIGALRM
signal.signal(signal.SIGALRM, handler)

# Set the timer to go off in 2 seconds
signal.setitimer(signal
