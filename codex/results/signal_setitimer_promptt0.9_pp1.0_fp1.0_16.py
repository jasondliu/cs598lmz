import signal
# Test signal.setitimer() and signal.getitimer() for the three
# timer types.
for timer in [signal.ITIMER_REAL, signal.ITIMER_VIRTUAL, signal.ITIMER_PROF]:


    def alarm_handler(a, b):
        alarm_count[0] += 1
        if alarm_count[0] == 2:
            raise KeyboardInterrupt


    # Test that out of range values to setitimer raise OSError.
    try:
        signal.setitimer(timer, -1, 0)
    except OverflowError:
        pass

    try:
        signal.setitimer(timer, 0, -1)
    except OverflowError:
        pass
    except ValueError:
        pass

    try:
        signal.setitimer(timer, -1, -1)
    except OverflowError:
        pass

    # Test that setting and getting the timer returns the correct value.
    signal.setitimer(timer, 5, 10)
    s = signal.getitimer(timer)
    assert s.interval ==
