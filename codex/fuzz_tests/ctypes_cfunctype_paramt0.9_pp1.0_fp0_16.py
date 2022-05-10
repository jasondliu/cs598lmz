import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)

U, _ = sp.symbols("U t")
x0 = ctypes.c_double(0.)  # create ctypes, that on the other side will hold pointer to py_object
x1 = ctypes.c_double(0.)
Uct = ctypes.py_object(U)
to_res = ctypes.py_object(U_prime(U, _))
out = ctypes.c_double(0.)
func = FUNTYPE(lambda t0: model_f(t0, x0, x1, Uct, to_res, out))
func(0.)
print(x0.value, x1.value)
print(out.value)
</code>
i.e. have just three lines of code that transliterate your symbolic expressions into <code>ctypes</code> form.

