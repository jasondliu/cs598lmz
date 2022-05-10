import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
print(fun())

from ctypes import cdll
lib = cdll.LoadLibrary(None)
print(lib.time(None))

import ctypes
from datetime import date
today = date.today()
print(today)
print(ctypes.pythonapi.PyDateTime_FromDateAndTime(
  today.year, today.month, today.day,
  0, 0, 0, 0))

from datetime import date
import ctypes

def pydate_to_c_struct(pydate):
    return ctypes.pythonapi.PyDateTime_FromDateAndTime(
      pydate.year, pydate.month, pydate.day,
      0, 0, 0, 0)

def c_struct_to_pydate(c_struct):
    return date.fromtimestamp(
      ctypes.pythonapi.PyDateTime_AsTimestamp(c_struct))

def test():
    pydate = date(2013, 12, 31)
    c_struct = pydate_to_c_struct(pydate)
   
