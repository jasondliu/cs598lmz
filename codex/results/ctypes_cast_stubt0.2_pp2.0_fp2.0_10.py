import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import sys

def _mimport(name, level=1):
    try:
        return __import__(name, globals(), level=level)
    except:
        return __import__(name, globals())

_data = _mimport('_data')
_mdsarray = _mimport('mdsarray')
_mdsscalar = _mimport('mdsscalar')
_mdsdata = _mimport('mdsdata')
_mdsdescriptor = _mimport('mdsdescriptor')
_mdscompound = _mimport('mdscompound')
_mdscontext = _mimport('mdscontext')
_mdsbuilder = _mimport('mdsbuilder')
_mdsdispatch = _mimport('mdsdispatch')
_mdsarray = _mimport('mdsarray')
_mdsrecord = _mimport('mdsrecord')
_mdsvalue = _mimport('mdsvalue')
_mdssearch = _mimport('
