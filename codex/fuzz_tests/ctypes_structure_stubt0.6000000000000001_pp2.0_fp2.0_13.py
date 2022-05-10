import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_double()

s = S()
s.x = 0.5
s.y = 2.5

lib = ctypes.cdll.LoadLibrary('libtest.so')
lib.foo(ctypes.byref(s))
print(s.x)
print(s.y)
</code>
The result is:
<code>0.5
2.5
</code>
Why doesn't <code>s.x</code> get modified?


A:

You pass a pointer to <code>s</code>, but your function modifies the copy of that pointer. You need to declare <code>foo</code> as <code>void foo(S *s)</code> and pass a pointer to <code>s</code> like so:
<code>#include &lt;stdio.h&gt;

typedef struct {
  double x, y;
} S;

void foo(S *s) {
  s-&gt;x = 2.0;
  s-&
