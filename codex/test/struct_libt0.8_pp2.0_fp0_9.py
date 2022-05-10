import _struct
import datetime

def unpack(fmt, file):
    return _struct.unpack(fmt, file.read(calcsize(fmt)))

def read_timestamp(file):
    # Timestamps are stored as FILETIME.
    # The differences between various epoch dates are listed here:
    # http://www.epochconverter.com/date-and-time/epochs.php
    # I'm assuming they're actually UTC timestamps, since they don't
    # match the epochs listed.
    # Also not sure if there's any adjustments needed to convert
    # to UNIX timestamps (seconds vs. milliseconds, etc.)
    unix_epoch = datetime.datetime.utcfromtimestamp(0)
    windows_epoch = datetime.datetime(1601, 1, 1)
    windows_epoch_delta = unix_epoch - windows_epoch
    timestamp_delta = datetime.timedelta(microseconds=windows_epoch_delta.microseconds)


