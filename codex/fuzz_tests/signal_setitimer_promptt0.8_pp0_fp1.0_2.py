import signal
# Test signal.setitimer exists
has_itimer = hasattr(signal, 'setitimer')

if has_itimer:
    from signal import ITIMER_REAL, ITIMER_VIRTUAL, ITIMER_PROF, setitimer
    from signal import getitimer

    def get_clock():
        if _clock == 'process_time':
            return time.process_time()
        elif _clock == 'perf_counter':
            return time.perf_counter()
        elif _clock == 'time':
            return time.time()
        else:
            assert _clock == 'monotonic', _clock
            return time.monotonic()

    def set_clock(clock):
        global _clock
        _clock = clock

    def start_timer(period, repeat=False, unit=1.0):
        """Configure signal timer to fire after period/unit and repeat every
        period/unit.  The return value can be passed to cancel_timer.
        """
        realperiod = max(0.0, period)
        clock = get_clock
        if
