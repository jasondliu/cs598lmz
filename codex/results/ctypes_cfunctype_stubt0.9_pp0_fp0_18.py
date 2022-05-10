import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hi!"
x = fun()
print (x, type(x))

# from   compileall import *
# print (py_compile)
# py_compile(*test_support.get_test_args('test_compile.py'))
#
# import zlib
# print (zlib.crc32)
#
# print (test_support.get_test_args('test_compile.py'))
#

# print (sanity_test_constants())
# print (constants.TEST, constants.__file__)



# print ('dir(ctypes) =', dir(ctypes))
# print ('dir(all) =', dir(all))

# from constants import constants1
# from constants import *
# from constants import *
# print(globals())
# print (tuple(globals()))

# print (constants.constants1, constants.__file__)

# print (sys)
# print (sys.meta_path)
# print (sys.path_importer_cache)
