import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
try:
    print(ctypes.CField)
except TypeError:
    print("not supported")

import sys
print(' '.join(sorted(sys.builtin_module_names)))
print(sys.flags)
print(sys.float_info)
print(sys.int_info)
print(sys.hash_info)
print(sys.implementation)
print(sys.version_info)
print(sys.subversion)
print(sys.api_version)
print(sys.maxsize)
print(sys.maxunicode)
print(sys.byteorder)
print(sys.version)
print(sys.platform)
print(sys.executable)
print(sys.argv)
print(sys.path)
print(sys.path_hooks)
print(sys.path_importer_cache)
print(sys.warnoptions)
print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())
print(sys.getrecursionlimit())
print(sys.getcheckinterval())
print(sys.getwindows
