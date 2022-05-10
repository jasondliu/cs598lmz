import _struct

from miasm2.core.cpu import par_conv, gen_reg


def dump_regs(cpu, regs_ids):
    '''
    Dump the values of the registers
    @cpu: a miasm2 CPU instance
    @regs_ids: a list of registers ID
    '''

