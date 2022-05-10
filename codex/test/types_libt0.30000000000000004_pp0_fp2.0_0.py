import types
types.MethodType(lambda self: None, None, Dummy)

# Test for SF bug #1465409
try:
    import _thread
except ImportError:
    pass
else:
    import sys
    import time

    # This takes enough time that the other thread will definitely still be
    # running when we exit, thus giving us a good test for the atexit
    # behavior.
    def very_slow_function():
        time.sleep(2)

    def main():
        _thread.start_new_thread(very_slow_function, ())
        sys.exit(42)

    main()

# Test for SF bug #1476447
import sys
if hasattr(sys, 'gettotalrefcount'):
    import gc
    gc.collect()
