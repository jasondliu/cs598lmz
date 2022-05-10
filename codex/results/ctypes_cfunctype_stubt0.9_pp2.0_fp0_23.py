import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"
# %load_ext cython

#%load_ext line_profiler

df = pd.DataFrame(
     np.random.randint(0,100,size=(10000, 4)),
     columns=list('ABCD')
    )

df["E"] = 100
df["F"] = df["C"] + df["D"]
df["G"] = df["F"] + 1

#df.eval("F = C + D", inplace=True)
def f(a, b, c, d, e, f, g):
    return (a + b + c + d + e + f + g)
df.eval("H = f(A, B, C, D, E, F, G)")
df.head()
%%cython
cdef np.ndarray[np.int_t, ndim=2] arr;
arr = np.random.rand(100000, 100)
%%cython
cdef np.ndarray[np.int_t, ndim=1] A;
A = np.
