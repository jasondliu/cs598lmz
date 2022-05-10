from types import FunctionType
a = (x for x in [1])
a.__len__ = 3
ctypes.pythonapi.PyObject_Hash.restype = ctypes.c_longlong
print(ctypes.pythonapi.PyObject_Hash(a))
print(sys.hash_info)
a = type(FunctionType)
sys.setrecursionlimit(1314)
print(sys.getrecursionlimit())
print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())
from ctypes import CDLL, c_bool
from os import environ
from sys import version_info
from os.path import dirname, join
from distutils.sysconfig import get_config_var
from subprocess import Popen, PIPE
from datetime import datetime
def _check_python_shared_library_abi():
    # if libpython is a symlink, get the real path to python binary
    libpython_real = Popen(['realpath', '-T', environ['LD_LIBRARY_PATH'] + 'libpython' + version_info[0] + '.' + version_info[1] + '.
