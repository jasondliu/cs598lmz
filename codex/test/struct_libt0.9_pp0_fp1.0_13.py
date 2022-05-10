import _struct

PY3 = sys.version_info[0] == 3

def int_size():
    """
    This is the maximum size that an int can be, on this platform
    """

    return _struct.calcsize('O')

def py_ticks(time = None):
    """
    Return the number of platform-specific ticks since the start of the platform
    epoch (Jan 1 1970 for Unix/Linux, Jan 1 1904 for MacOSX and Jan 1 1601 for
    Windows) as a Python integer.

    If time is given (as milliseconds since the start of the epoch),
    convert it to platform ticks.

    Platform ticks are useful for computing deltas between local time and
    universal time, and for accessing platform-specific timing interfaces.
    See platform_ticks_to_python and plaform_ticks_to_universal for
    converting back to milliseconds since the start of the epoch

    Call Formats:

      ticks = py_ticks()
      ticks = py_ticks(ticks)
    """

