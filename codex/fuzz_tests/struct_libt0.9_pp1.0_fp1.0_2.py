import _struct
import _json
import _math
import _cstruct
import time
import _random
import hashlib

import _types

from pythonista import _restrict_once
_restrict_once('RuntimeError("Access restricted")')


"""
Built-in builtins
"""

def abs(x):
  if isinstance(x, complex):
    return  _math.sqrt(x.real * x.real + x.imag * x.imag)
  return x.__abs__()

class bool():
  def __new__(t, x=None):
    if x is None: return None
    return True if __builtin__.bool(x) else False

def chr(n): 
  if n < 0 or n > 1114111:
    raise ValueError("chr() arg not in range(1114112)")
  return _types.string_type(unichr(n))

def complex(x=0, y=0):
  return cmp(x, y)
  
def dir(): 
  raise NotImplementedError
