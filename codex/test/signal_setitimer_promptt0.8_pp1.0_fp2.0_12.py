import signal
# Test signal.setitimer, which sets a timer to deliver a signal at some
# point in the future.  Repeatedly set it for smaller and smaller
# intervals and make sure it delivers the signal close to on time.

# XXX This will fail if the process takes more than about 10 seconds
# total to run.  setitimer only has microsecond resolution and the
# clock isn't that precise, so the process could take long enough that
# the timer underflows.

# This test isn't reliable enough to enable by default; see the XXX
# at the top of the file.
def disabled_test_setitimer(self):
    # Set up the alarm handler
    got_it = []
    def alarm(signum, frame):
        got_it.append(None)
        raise KeyboardInterrupt

    # And the signal handler to deliver SIGALRM
    signal.signal(signal.SIGALRM, alarm)

    # Loop a bunch of times, each time sleeping for less time.
