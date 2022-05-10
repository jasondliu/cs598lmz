import signal
# Test signal.setitimer()
#
# This test is not very good, because it relies on the fact that we
# don't have any other timers running.  It is not even guaranteed that
# we don't have any other timers running.
#
# This test is also not good, because it relies on the fact that we
# are not running on a broken system.  On a broken system, the signal
# might be delivered before we set the timer.  On a broken system, the
# signal might be delivered after we set the timer, but before we
# start the event loop.  On a broken system, the signal might be
# delivered after we set the timer, but after we start the event loop.
# On a broken system, the signal might be delivered after we set the
# timer, but before we start the event loop, but after we call
# signal.setitimer().
#
# This test is also not good, because it relies on the fact that we
# are not running on a very slow machine.  On a very slow machine, the
# signal might be delivered after we set the timer, but before we
# start the event loop.  On a very
