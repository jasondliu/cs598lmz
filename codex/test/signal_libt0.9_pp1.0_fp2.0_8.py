import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Trying to deal with type hinting on Travis by uninstalling `typing`.
# Anaconda3 has a different version of type hinting
# Raises an error in anaconda version 3.5
try:
    import typing
    import sys

    # This module will throw error if it is not uninstalled.
    # See http://docs.python.org/3/library/typing.html
    sys.modules.pop('typing')
except:
    pass

