import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.POINTER(ctypes.c_double), ctypes.c_int)

def register(f, dll):
    reg_f = FUNTYPE(f)
    dll.register_function(reg_f)

def sum_py(x, n):
    return np.sum(x)

def sum_c(x, n):
    return sum_c.lib.my_sum(x, n)

def sum_c_py(x, n):
    return sum_c_py.lib.my_sum_py(x, n)

def main():
    lib = ctypes.cdll.LoadLibrary('./libsum.so')
    print('sum_py(x,n) = ', sum_py(x,n))
    print('sum_c(x,n) = ', sum_c(x,n))
    print('sum_c_py(x,n) = ', sum_c_py(x,n))
    print('sum_c_py(x,n) = ', sum
