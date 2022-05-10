import weakref
import itertools
import numpy as np
import qcodes.utils.helpers as helpers
import qcodes.utils.validators as validators


class _LastEdit(object):

    def __init__(self, key, value, timestamp, serial):
        self.key = key
        self.value = value
        self.timestamp = timestamp
        self.serial = serial


class _Savepoint(object):

    def __init__(self, key, value, timestamp, serial):
        self.key = key
        self.value = value
        self.timestamp = timestamp
        self.serial = serial


class _Snapshot(object):

    def __init__(self, key, value, timestamp, serial, expid):
        self.key = key
        self.value = value
        self.timestamp = timestamp
        self.serial = serial
        self.expid = expid


class _Statistics(object):

    def __init__(self, key, value, timestamp, serial, expid):
        self.key = key
        self.value = value
       
