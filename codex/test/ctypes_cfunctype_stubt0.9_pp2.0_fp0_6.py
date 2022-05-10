import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): 
    return None

class A: 
    pass

def set_fun(x): 
    x.fun = fun

def main(n): 
    for i in range(n): 
        a = A() 
        assert not hasattr(a, 'fun')
        set_fun(a)

main(10**8)        
# fun at <ipython-input-1-d644d975fea9>:3
# set_fun at <ipython-input-1-d644d975fea9>:9
# range at rangebuiltin
# main at <ipython-input-1-d644d975fea9>:15
# <module> at <ipython-input-1-d644d975fea9>:18
# fun at <ipython-input-1-d644d975fea9>:3
# set_fun at <ipython-input-1-d644d975fea9>:9
# A at <ipython-input-1-d644d975fea9>:12
# main at <ipython-input-1
