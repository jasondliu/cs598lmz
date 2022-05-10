import signal
# Test signal.setitimer(2, 0.05, 0.1) and the SIGALRM
# it raises.
#
# _sig() is called in response to the SIGALRM, and we
# use setitimer(2) to arm the SIGALRM to raise every
# 0.05 seconds.
#
# sigs_received++ is incremented within each what() of
# SIGALRM, and tells how many SIGALRMs were recieved
# within the _sig() handler function.
#
_sigs_received = 0
def _sig(signum, frame):
  global _sigs_received
  _sigs_received += 1

#signal.signal(signal.SIGALRM, _sig)
#signal.setitimer(2, 0.05, 0.1)

# Wait for the SIGALRM to arrive.
#
# We use a while statement to print a '.' and check if
# the SIGALRM has arrived.  Delay for as close to .2
# seconds as possible using the sleep() function within
# the time module.
#
#
