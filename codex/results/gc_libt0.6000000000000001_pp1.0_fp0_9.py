import gc, weakref

from miasm.expression.expression import *
from miasm.expression.simplifications import expr_simp
from miasm.arch.arm.arch import mn_arm
from miasm.arch.arm.regs import regs_init
from miasm.arch.arm.regs import *
from miasm.core.asmblock import AsmBlockBad
from miasm.core.locationdb import LocationDB
from miasm.analysis.machine import Machine
from miasm.core.sembuilder import SemBuilder
from miasm.jitter.jitload import log_func

class ir_a_arml(ir):
    """IR for ARM little-endian"""

    def __init__(self, symbol_pool=None):
        ir.__init__(self, mn_arm, 32, 32, symbol_pool)
        self.ret_reg = self.arch.regs.R0

    def get_ir(self, instr):
        # no need to check instructions validity
        # (cf machine.py)
        pc_o = self.arch.pc.size /
