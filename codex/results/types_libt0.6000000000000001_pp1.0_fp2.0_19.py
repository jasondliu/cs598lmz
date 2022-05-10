import types
types.__all__.remove('ClassType')
types.__all__.remove('FunctionType')
types.__all__.remove('InstanceType')
types.__all__.remove('MethodType')
types.__all__.remove('UnboundMethodType')
types.__all__.remove('TypeType')
types.__all__.remove('BuiltinFunctionType')
types.__all__.remove('BuiltinMethodType')
types.__all__.remove('ModuleType')
types.__all__.remove('XRangeType')

# replace the types module with these new ones
del sys.modules['types']
sys.modules['types'] = types

# set the new sys.version
sys.version = '2.7.0'

# import the new modules
import warnings
warnings.filterwarnings('ignore', '.*', DeprecationWarning, 'warnings')
import site
import os
import errno
import posix
import posixpath
import stat
import genericpath
import fnmatch
import shutil
import copyreg
import linecache
import re
import sre_
