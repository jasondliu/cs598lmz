import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    raise Exception('abc')

try:
    fun()
except Exception as exc:
    print(exc)
else:
    print('success')
    
    
    
    
    
    
    
    
    
    
    
def wrapexcp(fun):
    import ctypes
    fp = ctypes.CFUNCTYPE(ctypes.py_object)(fun)
    def gfun():
        try:
            return fp()
        except:
            import sys
            print('print from wrapper',file=sys.stderr)
    return gfun
 
@wrapexcp
def fun():
    raise Exception('abc')

try:
    fun()
except Exception:
    print('success')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
