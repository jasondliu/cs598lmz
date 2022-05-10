import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class A(object):
    def __init__(self):
        self.fun = FUNTYPE(self.fun)
    def fun(self):
        return None

def main():
    a = A()
    print a.fun()
    print fun()

main()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 18, in &lt;module&gt;
    main()
  File "test.py", line 16, in main
    print a.fun()
TypeError: 'CFUNCTYPE' object is not callable
</code>
I don't understand why the first call to <code>a.fun()</code> works and the second call to <code>fun()</code> doesn't.


A:

<code>a.fun</code> is a <code>CFUNCTYPE</code> object, not a function.  You need to call it with the <code>()</code> operator:
<code>print a.fun()()
