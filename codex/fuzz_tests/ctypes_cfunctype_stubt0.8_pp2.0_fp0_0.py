import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 10

fun.__name__ = "name"
import dis
dis.dis(fun)
</code>
Output:
<code>Disassembly of &lt;function name at 0x7f5e14e038c8&gt;:
  5           0 LOAD_GLOBAL              0 (fun)
              3 CALL_FUNCTION            0
              6 RETURN_VALUE
</code>

