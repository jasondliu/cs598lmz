import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def is_learning_env():
    # currently true if not on windows, unless GUPPY_FORCE_WINenvir=1
    return not sys.platform == "win32" or os.environ.get('GUPPY_FORCE_WINenvir')=='1'


#############
## LEARNING STRATEGY
#
# FilesystemArrays at the root level.
#
# LearningStrategy contains a list of
# (name, shape, dtype) tuples. All arrays in the tuple have the same shape but they can be
# different dtypes, and they have different names.
#
# In the filesystem backend, the arrays resident in memory are written using multiple files,
# the number of files is determined by the number of items in the tuple. So a LearningStrategy
# with a single tuple containing three arrays will be six files total (one file per array item).
#
# All the stuff in the tuple is written out, starting at 2**20 in all Farrays, and then again,
# starting at 1/2 of all Farrays up to 2**
