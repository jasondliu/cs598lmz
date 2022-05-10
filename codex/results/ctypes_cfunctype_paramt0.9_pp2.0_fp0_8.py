import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_double , ctypes.c_double )
ADDFUN = FUNTYPE( lambda x: x + 1.0 )
print( "In python: Calling %g + 1.0 = %g" % (3.1415, ADDFUN( 3.1415 )) )
addfun_lib.call_addfun(ADDFUN , 3.1415 )


print("""
==============================================================
F m easure.c / ffi-wasm-demo
==============================================================
""")
import time
import measure

t0 = time.time()
measure.wasm_demo()
t1 = time.time()
print("First call to wasm took %g seconds" % (t1-t0))

t0 = time.time()
measure.wasm_demo()
t1 = time.time()
print("Second call to wasm took %g seconds" % (t1-t0))

t0 = time.time()
measure.wasm_demo()
t1 = time.time()
print("Thi
