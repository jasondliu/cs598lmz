import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print "hello"
cfun = fun.__code__
fun <=> ctypes.pythonapi.PyEval_EvalCode
cfun.co_argcount <=> 0
cfun.co_filename <=> "(none)"
cfun.co_name <=> "fun"
cfun.co_names <=> []
cfun.co_nlocals <=> 1
cfun.co_varnames <=> ('fun',)

cfun.co_cellvars <=> ()
cfun.co_freevars <=> ()
cfun.co_code <=> 'd\x00\x00Z\x00\x00d\x01\x00S'
cfun.co_firstlineno <=> 1
"hi"
cfun.co_consts <=> ()
cfun.co_lnotab <=> '\x00\x01\x0b\x00'
cfun.co_stacksize <=> 2
cfun.co_flags <=> 67

exec("""
def fun():
   pass
""")
cfun =
