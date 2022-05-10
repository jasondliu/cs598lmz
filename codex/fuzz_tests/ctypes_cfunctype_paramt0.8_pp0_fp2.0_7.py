import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)


class _Signals(object):

    _SIG_DFL = 0
    _SIG_IGN = 1

    def __init__(self):
        self._signal_handlers = {}
        self._default_signal_handlers = {}

    def add_signal_handler(self, signal, handler):
        # Trying to use the SIG_DFL or SIG_IGN constants in here causes
        # a segfault on some platforms.
        # It seems to be related to the definition of the two constants and
        # the order in which things are imported.
        #
        # We can call the function directly, though.
        #
        # See https://github.com/celery/celery/issues/4105
        try:
            self._default_signal_handlers[signal] = signal.getsignal(signal)
        except AttributeError:
            self._default_signal_handlers[signal] = signal.default_int_handler
        signal.signal(signal, handler)
        self._signal_handlers
