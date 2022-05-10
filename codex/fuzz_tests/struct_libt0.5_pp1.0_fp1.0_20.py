import _struct

from miasm2.core.cpu import par_conv, gen_reg


def dump_regs(cpu, regs_ids):
    '''
    Dump the values of the registers
    @cpu: a miasm2 CPU instance
    @regs_ids: a list of registers ID
    '''

    for reg_id in regs_ids:
        print "*" * 80
        print "*", reg_id
        print "*" * 80
        for mode in cpu.modes:
            print "  *", mode
            reg = getattr(cpu.arch.regs, reg_id)
            if mode in reg.modes:
                reg_off = reg.modes[mode]
                print "    - offset:", reg_off
                print "    - content:", reg.content[reg_off]


def reg_and_id(cpu, reg_id):
    '''
    Get the offset and the size of a register in the current mode
    @cpu: a miasm2 CPU instance
    @reg_id: a register ID

