import signal
# Test signal.setitimer():
#
# This test is a modified version of a test found at
# http://mail.python.org/pipermail/python-bugs-list/2001-September/003820.html
#
# The problem here was that the signal handler was not called if the process
# was blocked in a syscall.  The solution is to use a handle_signal() function
# that actually interrupts the syscall.
#
# This test is a bit tricky: we need to be sure that the syscall is actually
# blocked when we send the signal because the alarm() function is not
# guaranteed to be precise (it will be precise in Linux but may not be in
# other OSes).
#
# So we set the alarm to be two seconds in the future, and we wait for two
# seconds in the syscall so that the alarm should be there just when the
# syscall is blocked.  Then we send the alarm and we check that the handler
# was called.
#
# This test is known to fail on Windows (on Windows, it seems that the
# ITIMER_REAL timer is actually emulated
