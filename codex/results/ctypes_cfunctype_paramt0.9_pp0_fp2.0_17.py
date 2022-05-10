import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.POINTER(c_int))
var = c_int(42)
def myfun(var):
    print "myfun:",var.contents.value
fun = FUNTYPE(myfun)
fun(var)

# ======================================================================
#         Name:  decoder
#
#  Description:
#
#       Return:
# ======================================================================
def decoder(func, address, const, regs):
    if func.offset == address:
        return func.name + ":"
    for i in range(len(func.xrefsFrom)):
        inst = func.get_instruction_at(address)
        tmp_inst = inst
        if inst.mnemonic != "call" or not inst.is_call:
            for i in range(const):
                tmp_inst = tmp_inst.prev
                if tmp_inst.mnemonic == 'call':
                    inst = tmp_inst
                    break
        if i == len(func.xrefsFrom):
            return ""
        if inst.operands[0].value == func.x
