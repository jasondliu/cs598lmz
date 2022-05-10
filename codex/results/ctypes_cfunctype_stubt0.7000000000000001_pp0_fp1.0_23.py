import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

# This is a C-level cast, so it doesn't use the python level __int__ method
result = hash(fun)
print(result)
</code>
Returns
<code>36
</code>
(Note: if you hash the functor itself, you get a different answer: <code>140554343998304</code>, which is the default hash of an object)

