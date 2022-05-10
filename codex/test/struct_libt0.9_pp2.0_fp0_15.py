import _struct

from pypy.jit.codewriter.effectinfo import EffectInfo
from pypy.jit.metainterp.history import AbstractDescr
from pypy.rpython.lltypesystem import lltype, rffi
from pypy.rpython.ootypesystem import ootype
from pypy.jit.metainterp.resoperation import rop
from pypy.jit.backend.llsupport.symbolic import WORD
from pypy.jit.backend.llsupport import symbolic


class CallDescr(AbstractDescr):
    def __init__(self, RESULT):
        self.RESULT = RESULT
        self.size_call_args = None
        self.float_Arg = False
        self.write_descr_off = None
        self.arg_classes = [rffi.CCHARP]

    def get_result_type(self):
        return self.RESULT

    def get_index(self):
        return self.index

    @staticmethod
    def _freeze_(arg):
        return True
