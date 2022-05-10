import gc, weakref, traceback, sys, re, threading, heapq
from functools import partial
from itertools import imap, repeat
import pypy.rpython.rlist
import pypy.rpython.rmodel
import pypy.rpython.rbuiltin
from pypy.rlib.rarithmetic import ovfcheck
import pypy.rlib.objectmodel
from pypy.objspace.std.celldict import ModuleDictStrategy
from pypy.objspace.std.model import registerimplementation, W_Object
from pypy.objspace.std.stdtypedef import StdTypeDef, SMM
from pypy.objspace.std.basestringtype import basestring_typedef
from pypy.objspace.std.settype import set_typedef, frozenset_typedef
from pypy.objspace.std.tupletype import tuple_typedef
from pypy.objspace.std.inttype import int_typedef
from pypy.objspace.std.sliceobject import
