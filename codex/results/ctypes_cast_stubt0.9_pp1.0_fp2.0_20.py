import ctypes
ctypes.cast(id(myfunc), ctypes.py_object).value

if(globals().has_key('myfunc')):
    myfunc()

# def printSpam():
#     print 'Ham'
#
# printSpam.instance_class = None
# printSpam.__doc__ = "This is a test."
# printSpam.__name__ = "Hahaha"
# printSpam.__module__ = "TheModule"
