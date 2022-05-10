import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_longlong,ctypes.c_longlong)
FUNPTR = ctypes.POINTER(FUNTYPE)
func = ctypes.cdll.LoadLibrary('./baz')
func.foo.restype = FUNPTR
func.bar.restype = FUNPTR

A = np.zeros((32,16))
foo = func.foo()
bar = func.bar()

A[4,4] = foo(4,4)
A[4,12] = bar(4,12)
</code>
C Code:
<code>#include &lt;stdio.h&gt;
typedef double(*functype)(long long,long long);
double foo(long long i, long long j) {
  return (double)i+j;
}
double bar(long long i, long long j) {
  return (double)i*j;
}
functype foo_ptr() {
  return &amp;foo;
}
functype bar_ptr() {
  return &amp
