import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
l = (1,2,3)
f = FUNTYPE(lambda : l)
f()
 
#Swig also supports nested tuples, e.g. ()()
SWIG_PACKAGE = 'swig_depth_3'

from ctypes import *
from nose.tools import eq_,ok_
from sys import stderr
from test_support import *

import sys
if sys.platform == 'cli':
  CLILIB = r'depth_2\bin\Release\depth_2.dll'
  from System.Runtime.InteropServices import DllImportAttribute, MarshalAsAttribute
  INTERCLR_DLL_IMPORTS_MAP = {
      "depth_2.dll": [
        ("depth_2.depth_2_functions", "depth_2", DllImportAttribute(CLILIB)),
        ("depth_2.depth_2_functions", "convert2DotNetString", DllImportAttribute(CLILIB)),
       ]
    }
  sys.path.append(prefix+r'd
