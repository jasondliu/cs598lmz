import signal
# Test signal.setitimer()
class Alarm(Exception):
    pass
def alarm_handler(signum, frame):
    raise Alarm
signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)    # Schedule the first alarm for 0.1 seconds
try:
    while True:
        print 'not yet'
except Alarm:
    print 'Alarm!'
# End of signal.setitimer() test

#del sys.path[0]

# TODO: change this to import from __main__?
import __main__ as main

# Set up a dictionary to serve as the environment for the shell, so
# that tab completion works on modules under the current directory
import os, sys
env = dict(__name__="__console__", __doc__=None, __package__=None)
#env = {}
env.update(os.environ)
sys.path.insert(0, '')

# Add the current directory to the module search path.
sys.path.insert(0,
