import signal
# Test signal.setitimer
#
# This test is for the case where the signal handler is called from
# within a signal handler.

# This is a signal handler.
#
def handler(signum, frame):
    # This is a signal handler.
    #
    def handler2(signum, frame):
        # This is a signal handler.
        #
        def handler3(signum, frame):
            # This is a signal handler.
            #
            def handler4(signum, frame):
                signal.setitimer(signal.ITIMER_REAL, 0.5)
                signal.signal(signal.SIGALRM, signal.default_int_handler)
            signal.setitimer(signal.ITIMER_REAL, 0.5)
            signal.signal(signal.SIGALRM, handler4)
        signal.setitimer(signal.ITIMER_REAL, 0.5)
        signal.signal(signal.SIGALRM, handler3)
    signal.setitimer(signal.ITIMER_REAL,
