import mmap
import os
import re
import signal
import socket
import sys
import time

from optparse import OptionParser

from nagiosplugin import (
    CheckError,
    Check,
    Metric,
    Resource,
    ScalingAdapter,
    Summary,
    Timeout,
    )

class TimeoutError(Exception):
    pass

class FileScalingAdapter(ScalingAdapter):
    def __init__(self, *args, **kwargs):
        ScalingAdapter.__init__(self, *args, **kwargs)
        self.last_value = None
        self.last_time = None

    def get_value(self):
        if self.last_value is not None:
            interval = (self.last_time - time.time()) / 60
            return self.last_value / interval
        return self.last_value

    def set(self, value):
        self.last_value = value
        self.last_time = time.time()

class ConntrackCheck(Check):
    def __init__(self, *args
