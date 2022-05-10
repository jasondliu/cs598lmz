import signal
# Test signal.setitimer to test periodic processes
import logging

#from sutil import deco_timer, obj2nvh_recurse
from sutil     import obj2nvh_recurse, deco_timer, dumpperiod
from zmqutil   import zpipe
import zmq      as zmq
 
def sig_handler(sig, frame):
    if sig == signal.SIGINT:
                print "Got SIGINT!"
                sys.exit(-1)
    elif sig == signal.SIGCONT:
        print "Got SIGCONT!"
    else:
        print "Got signal ", sig

def sig_handler_alarm(signum, stack):
    print 'Alarm in sig_handler_alarm'

signal.signal(signal.SIGINT, sig_handler)
signal.signal(signal.SIGCONT, sig_handler)
signal.signal(signal.SIGALRM, sig_handler_alarm)

#sys.exit(0)
    
def main():
    # Message passing pipeline
    # msg is a
