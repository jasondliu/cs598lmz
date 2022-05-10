import mmap
import os
import pytest
import re
import sqlite3

from chaossystemd import meta


class Custom_data(object):

    def __init__(self, name, value):
        self.value = value
        self.name = name
        self.start_time = None
        self.end_time = None
        self.duration_seconds = None
        self.duration_microseconds = None
        self.invocation_id = None
