import mmap
import sys
import time
import os
import re

# The following global variable is used to hold the mapping between the
# device name and the device file path.
dev_name_to_file = None

# The following is a list of optional fields to be retrieved from the
# ftrace event fields.
optional_event_fields = ['tid', 'name']

# The following global variable is used to hold the mapping between
# the device name and the device file path.
dev_name_to_file = None


def parse_time(fstr):
    """
    This function parses the specified time string, which is in the format
    of "year-month-day hour:minute:second" and returns the corresponding
    time in seconds since the epoch.
    """

    # The following line generates the time structure based on the specified
    # time.
    ts = time.strptime(fstr, '%Y-%m-%d %H:%M:%S')

    # The following line converts the time structure to the time in seconds
    # since the epoch.
    return time
