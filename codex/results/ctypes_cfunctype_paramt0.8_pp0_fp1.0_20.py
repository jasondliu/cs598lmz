import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

def array_from_data(data):
    arr = (ctypes.c_double * len(data))(*data)
    return arr

def test(data, func):
    arr = array_from_data(data)
    num = func(len(data), arr, 2)
    return num

with open("libcall.so", "rb") as f:
    dll = ctypes.CDLL(f.name)

func = FUNTYPE(dll._Z3funiPdi)(3)
print(test([1,4,7],func))
</code>

