import signal
# Test signal.setitimer()

# This test program is a bit of a mess, but it's the best we can do on
# Windows.  The problem is that we want to test the behaviour of
# setitimer() with a signal handler that raises an exception.  On
# Windows, if we raise an exception in a signal handler, the handler is
# simply disabled, and the exception is ignored.  So we need to raise
# the exception in a thread.  But if we do that, we can't be sure that
# the signal handler will be invoked before the exception is raised.
# So we need to use a thread that raises the exception after a delay.
# But threads are not interruptible on Windows, so the thread may not
# be interrupted by the signal.
#
# So, we use a thread that raises an exception after a delay, and we
# use a signal handler that raises an exception immediately.  If the
# signal handler is invoked, then the exception will be raised in the
# signal handler, and the thread will not raise an exception.  If the
# signal handler is not invoked, then the thread will raise an
# exception, and the signal handler will
