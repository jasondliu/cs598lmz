import types
# Test types.FunctionType
try:
    cw(types.FunctionType)
    raise Exception("Should have raised a TypeError")
except TypeError, e:
    pass


import sys
if sys.version_info > (2, 5):
    # Test types.GeneratorType
    try:
        cw(types.GeneratorType)
        raise Exception("Should have raised a TypeError")
    except TypeError, e:
        pass

import types
# Test types.InstanceType
try:
    cw(types.InstanceType)
    raise Exception("Should have raised a TypeError")
except TypeError, e:
    pass

import weakref
# Test types.MethodType
try:
    cw(types.MethodType)
    raise Exception("Should have raised a TypeError")
except TypeError, e:
    pass

sys.stdout.write("Doing types.InstanceType tests ")

# This function is needed because __eq__ isn't
# picklable
def eq(a, b):
    return a == b

class Bar(object):
    def __init__
