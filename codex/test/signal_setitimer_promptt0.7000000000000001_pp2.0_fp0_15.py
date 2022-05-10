import signal
# Test signal.setitimer()
#
def setitimer(which, seconds, interval=0):
    """
    Calls signal.setitimer() and prints a message
    """
    print('  setting %s timer for %d seconds, interval %d' % \
          (which, seconds, interval))
    signal.setitimer(which, seconds, interval)

def alarm_handler(signum, frame):
    """
    Handler for SIGALRM
    """
    print('Alarm handler called with signal %s' % signum)
    setitimer('ALRM', 1, 1)

def profile_handler(signum, frame):
    """
    Handler for SIGPROF
    """
    print('Profile handler called with signal %s' % signum)

def main():
    """
    Main program: install handlers and set timers
    """
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.signal(signal.SIGPROF, profile_handler)
    setitimer('ALRM', 1, 1)
