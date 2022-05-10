import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_uint64, ctypes.c_uint64)

def asm(code):
    asm_lib = ctypes.CDLL('./asm_lib.so')
    asm_lib.asm.restype = FUNTYPE
    asm_lib.asm.argtypes = (ctypes.c_char_p, )
    f = asm_lib.asm(code)
    return f

def to_hex(data):
    b = bytearray(data)
    res = ''
    for ch in b:
        res += '0x{:X}, '.format(ch)
    return res

def print_code(code):
    print(marked_code(asm(code), 'x86-64'))
    print('')

def benchmark(code):
    @jit
    def inner(n):
        f = asm(code)
        res = 0
        for i in range(n):
            res += f(i)
        return res

    n = 100000000
    time_jit = timeit.timeit
