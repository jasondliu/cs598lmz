import signal
# Test signal.setitimer(signal.ITIMER_PROF, 10, 0)
# ITIMER_PROF: profile interrupt.
# second param is how often the timer should fire
# third param is how many seconds until the timer should first fire.
#
# NOTE: You must call signal.setitimer() twice to reset the timer.
#
# NOTE: .profile_threshold must be set.
#
# NOTE: You must call signal.setitimer() in the main thread,
#       otherwise the profiler will not work.

#-------------------------------------------------------------------------------
#

def test_setitimer():
    signal.setitimer(signal.ITIMER_PROF, 10, 0)
    #
    # NOTE: You must call signal.setitimer() twice to reset the timer.
    signal.setitimer(signal.ITIMER_PROF, 10, 0)
    #
    # NOTE: .profile_threshold must be set.
    cProfiler.the_profiler.profile_threshold = 0.1
    #
    # NOTE: You must call signal.setitimer()
