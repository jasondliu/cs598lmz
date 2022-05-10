import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_uint32)


class Ticker(object):
    """
    A simple class for creating a callback at regular intervals.

    Arguments:
        interval:   The time between calls in seconds.
    """

    def __init__(self, interval):
        self._interval = interval
        self._last = 0
        self._callback = None
        self._callback_args = []

    def set_callback(self, callback, *args):
        """
        Sets the callback and its arguments.

        Arguments:
            callback:   A callable to call.
        """
        self._callback = callback
        self._callback_args = args

    def tick(self, time_now):
        """
        Check if the ticker should be called.

        Arguments:
            time_now:   The current time.
        """
        if time_now > self._last + self._interval:
            self._last = time_now
            if self._callback:
                self._callback(*self._callback_args)


class Game(object):
    """
