import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return {str(i): i for i in range(2000)}

t0 = time()
for i in range(1000):
    fun()()
print("py_object:\t%f" % (time() - t0))
</code>
I get:
<code>py_object:   0.149635
ctypes:      0.110526
</code>
Not quite as much speedup as you have...

