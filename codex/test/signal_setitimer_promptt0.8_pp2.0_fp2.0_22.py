import signal
# Test signal.setitimer()
#
def sighandler(signum, frame):
    print('Got signal', signum, 'at', frame)
    signal.alarm(30)

# Display the signal name for all signals except SIGALRM
signames = dict((k, v) for v, k in signal.__dict__.iteritems()
                if v.startswith('SIG') and not v.startswith('SIG_'))
signal.alarm(2)
print('Setting alarm for 2 secs')
signal.signal(signal.SIGALRM, sighandler)
print('Waiting for first signal')
signal.sigwait([signal.SIGALRM, signal.SIGINT])
print('Waiting for next signal')
signal.sigwait([signal.SIGALRM, signal.SIGINT])
print('Waiting for next signal')
signal.sigwait([signal.SIGALRM, signal.SIGINT])
print('Waiting for next signal')
