import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
def set_interval(interval, times = -1):
    """Execute function at an interval.
       Execute function at every <interval> second, <times> amount of times.
    """

    # This is the function that will be called
    def func_wrapper():
        """This is the wrapper that gets passed to the setTimeout call."""
        set_timeout(interval, func_wrapper)
        func()

    def set_timeout(interval, func, *args):
        """Execute function at the next interval."""
        # Convert interval to ms
        secs = interval * 1000
        # Call the ctypes timers, passing our timer function as the callback.
        c_func = FUNTYPE(func)
        # Our ctypes callback must have it's argtypes defined, or it
        # won't work. We pass argtypes as None because we don't know
        # what args the user is going to provide to the function.
        c_func.argtypes = [FUNTYPE]
        pygame.time.set_timer(pygame.USEREVENT, int
