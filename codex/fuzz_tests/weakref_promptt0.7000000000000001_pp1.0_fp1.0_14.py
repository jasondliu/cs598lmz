import weakref
# Test weakref.ref(target)
# Test weakref.ref(target, callback)
import weakref
import operator
import gc
import time, sys

class MyObj:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyObj(%s)' % self.name

class MyObj2:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyObj2(%s)' % self.name

class MyObj3:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyObj3(%s)' % self.name

class MyObj4:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyObj4(%s)' % self.name

class MyObj5:
    def __init__(self, name):
        self.name = name

