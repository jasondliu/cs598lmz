import signal
# Test signal.setitimer
# This works on FreeBSD and Linux, but not Cygwin
# Windows only has the alarm() function, which only allows one
# outstanding timer.
#
# No way to test whether it works, except that it doesn't raise an
# exception.
signal.setitimer(signal.ITIMER_REAL, 0.2)
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.2)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.2, 0.2)
signal.setitimer(signal.ITIMER_PROF, 0.2)
signal.setitimer(signal.ITIMER_PROF, 0.2, 0.2)

