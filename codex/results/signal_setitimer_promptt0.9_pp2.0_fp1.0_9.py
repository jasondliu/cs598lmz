import signal
# Test signal.setitimer on Linux.


# It is hard to test when the timer expires.  We sleep in between
# setting the timer and receiving its signal.  It is good enough to
# make quick tests that ITIMER_REAL works as expected.  For more
# thorough tests, use something like
#
#   perf stat -r 10 sleep 0.1
#
# to make sure the timer expiration is measured correctly.

# The loop in this test is because
#
#   1. We want to test the case where a timer fires while the handler
#      is executing, but if we just have 2 test cases, the chance is
#      relatively small that the timer fires between the time we
#      invoke .setitimer() and the time we block waiting for another
#      signal.
#
#   2. For the case where we test ITIMER_REAL < ITIMER_REAL, we need
#      a loop because at some point we need to make sure that we've
#      received the timer signal from (1).  Otherwise, at the end of
#      the test, the program won't exit on the timer signal.

