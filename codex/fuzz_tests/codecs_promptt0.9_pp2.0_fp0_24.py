import codecs
# Test codecs.register_error method

import codecs
import StringIO

codecs.register_error("strict", codecs.strict_errors)

s = u"\xff"

out = StringIO.StringIO()
c = codecs.getwriter("ascii")(out, "strict")
try:
    c.write(s)
except UnicodeEncodeError, v:
    pass
else:
    raise ValueError, "problem not detected"
print v
print "Codec name: %s" % v.codec

"""
__test__['register_error#1']=\
"""
from codecs import register_error
import codecs
from copy import copy
import unittest

try:
    codecs.lookup_error('myerror')
except LookupError:
    pass
else:
    print 'should raise LookupError'

try:
    class myerror(Exception):
        def __init__(self, reason):
            self.reason = reason
        def __str__(self):
            return "myerror:" + self.reason

