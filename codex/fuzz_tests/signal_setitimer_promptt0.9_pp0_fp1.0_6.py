import signal
# Test signal.setitimer interval is 1e-7
signal.setitimer(signal.ITIMER_REAL, 1e-7, 1e-7)
# Check some mandatory properties of nanosecond sleep
assert not hasattr(signal.setitimer, '_QThread')
assert signal.setitimer.__module__ == 'imp'
# Check for temporary lazy-import added in Python 3.8
assert signal.setitimer.__code__.co_filename.endswith('_signal.py')
# Check for constant time with or without Python module
duration, expected_min, expected_max = 1/1e6 * 2, 0.95, 1.05
benchmarks = [(time.time,), (qtimer.nsleep,), (time.sleep, 1e-9)]
for f, *args in benchmarks:
    elapsed = min(timeit.repeat(f, setup='from __main__ import f, args; gc.enable()',
                                number=1000, globals=globals(), repeat=10, *args))
    print(f'{f.__name__}
