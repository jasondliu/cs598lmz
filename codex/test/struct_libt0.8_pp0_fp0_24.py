import _struct
import datetime
import logging
import os
import sys

# python 2.6 only
import json

import dateutil.parser
import dateutil.tz

#
# Time by itself doesn't do anything special.  It's a base class for
# other classes, like TimeOnDisk, to inherit from.
#
class Time(object):

    def __init__(self, value):
        self.value = value

    def __bytes__(self):
        return self.value

    def __unicode__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __long__(self):
        return long(self.value)

    def __float__(self):
        return float(self.value)

    def __repr__(self):
        return '{0}: {1}'.format(self.__class__.__name__, self.value)


