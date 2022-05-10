import codecs
# Test codecs.register_error
import sys
import errno
import weakref
import operator
import fcntl
import os
import tempfile
import pkgutil

class X :
    def __init__(self, a) :
        self.a = a
    def __eq__(self,other):
        return operator.is_(self.a,other.a)

class C(object):
    def __init__(self, a):
        self.a = a
    def __eq__(self,other):
        return self.a == other
    def __ne__(self,other):
        return self.a != other

class D(object):
    def __init__(self, a):
        self.a = a
    def __eq__(self,other):
        raise TypeError
    def __ne__(self,other):
        raise TypeError

#http://bugs.python.org/issue17498
import collections
CNT = 10 * 1000 * 1000
d = collections.deque()
for i in xrange(CNT):
    d.append(i)

