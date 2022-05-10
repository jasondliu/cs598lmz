import ctypes
ctypes.cast(1, ctypes.py_object)

#import sys
#sys.getrefcount(1)

#a = []
#b = a
#sys.getrefcount(a)

#del a
#sys.getrefcount(b)

#import weakref
#a = []
#b = weakref.ref(a)
#b()

#del a
#b()

#import weakref
#a = []
#b = weakref.ref(a)
#b()
#a.append(b)
#del a
#b()

#import weakref
#a = []
#b = weakref.ref(a)
#b()
#a.append(b)
#a = None
#b()

#import weakref
#a = []
#b = weakref.ref(a)
#b()
#a.append(b)
#a = None
#b()
#b()()

#import weakref
#a = []
#b = weakref.ref(a)
#b()

