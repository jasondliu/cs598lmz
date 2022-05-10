import signal
# Test signal.setitimer() which is currently not implemented in nympy.
# setitimer() expects callable object (callbacks) whereas signal() requires signal handler function
# so a class must be created to mimic named function (like signal handler)

class Cb_timers():                                                 # Raising SIGALRM which is processed 
    def __init__(self, Num_callbacks):                             # by its handler.
        self.Num_callbacks = Num_callbacks
        self.callbacks = []
        self.cnt = 0

    def add_handler(self, hdlr):                                   # Adds handler to be called int
        self.callbacks.append(hdlr)                                # added order

    def callback(self, signum, frame):
        self.cnt += 1
        print()
        print(time.asctime(), '==> Cb_timer:: Callback ', self.cnt, ' of ', self.Num_callbacks)
        for callback in self.callbacks:                            # Invoking handlers in the order
            callback()                                             # they where added
