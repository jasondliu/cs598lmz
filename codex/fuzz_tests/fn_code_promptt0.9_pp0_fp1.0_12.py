fn = lambda: None
# Test fn.__code__
try:
    import tkinter
except ImportError:
    # No Tk installed
    test_support.run_unittest(*test_cases)
else:
    # Prevent test_tk
    __import__ = lambda mod: None
    #  Tk installed
    test_support.run_unittest(*test_cases)
    del __import__
