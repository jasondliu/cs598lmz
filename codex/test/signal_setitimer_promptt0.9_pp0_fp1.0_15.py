import signal
# Test signal.setitimer
# Requires support for timerfd_create
#
# Shell usage: tst-timerfd-SIGUSR1 op timeout
#
# Setitimer calls:
# op is one of 0 (set/reset), ITIMER_REAL, ITIMER_VIRTUAL, ITIMER_PROF
# If op==0 then first use of setitimer(op, \&{}, \&{timeout,0}
# and after timeout use setitimer(op, \&{}, \&{}) to reset
# or set timer(s) again
#
# Timeout is one of: S.s, s, .s, or none (no setitimer)
# special values are:
# timeout=0.001s ==> short enough to prevent any other timer incident
# before the SIGUSR1
# timeout=500 ==> will probably cause a SIGUSR1 in the middle of execution
#
# The program should be started in the background.
# On a timeout SIGUSR1 will be raised.
# If no timeout is set then SIGUSR1 can be artificially raised
# to check if set
