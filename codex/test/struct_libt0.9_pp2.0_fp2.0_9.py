import _struct

from btypes import *
from symbol import Symbol, SymbolTable
from datatypes import *
from arrays import Array, FixedArray


#------------------------------------------------------------------------------
# PROCEDURES
#------------------------------------------------------------------------------


class Procedure(object):

    def __init__(self, type_=None, no_return=False, *args, **kwargs):
        super(Procedure, self).__init__(*args, **kwargs)
        self.type = type_
        self.params = []
        self.local = {}
        self.code = []
        self.no_return = no_return

    def add_param(self, param):
        self.params.append(param)

    def add_local(self, local):
        if local.name in self.local:
            raise ValueError(local.name)
        self.local[local.name] = local

    def add_code(self, code):
        self.code.append(code)


#------------------------------------------------------------------------------


class FormalParam(object):

    def __init__(self, type_, name):
        self
