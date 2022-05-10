import gc, weakref, types
from libtbx import group_args
from types import DictType, FloatType, IntType, ListType, NoneType, TupleType
from types import StringType, UnicodeType
from operator import itemgetter, truth
from copy import copy

class parameter_flag(object): pass

class parameter_defs(object):

  __slots__ = []
  width = 20
  key_format = "%-*s = "
  value_format = "%s\n"
  def __init__(self, *flags, **opt):
    def add_flag(obj, flag_name, value=None, doc=None):
      if(flag_name in opt):
        setattr(obj, flag_name, opt[flag_name])
      else:
        if(value is None): value = parameter_flag
        setattr(obj, flag_name, value)
      if(doc is not None):
        obj._docs[flag_name] = doc
    self._list = []
    self._dict = {}
    self._docs = {}
    obj = self

