import types
types.new_class("A", (object,))

from pypy.annotation import model as annmodel
from pypy.annotation.bookkeeper import getbookkeeper
from pypy.annotation.annrpython import RPythonAnnotator
from pypy.annotation.classdef import ClassDef, InstanceSource
from pypy.annotation.classdef import struct as struct_
from pypy.rpython.ootypesystem import ootype
from pypy.rpython.ootypesystem import rclass
from pypy.rpython.test.test_llinterp import interpret
from pypy.rlib.objectmodel import we_are_translated
from pypy.rlib.debug import debug_start, debug_print
from pypy.rlib.rarithmetic import r_longlong
from pypy.rlib.rarithmetic import r_ulonglong
from pypy.objspace.flow.model import Constant
from pypy.translator.translator import TranslationContext
from pypy.translator.simplify import get_graph
from p
