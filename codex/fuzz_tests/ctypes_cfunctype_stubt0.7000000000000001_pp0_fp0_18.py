import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Hello, World!")

dct = {"foo": fun}
data = pickle.dumps(dct)

# p1.py
dct2 = pickle.loads(data)
dct2["foo"]()
</code>
The code works as expected. However, if I change the definition of <code>fun</code> in <code>p1.py</code> to:
<code>@FUNTYPE
def fun():
    print("Hello, World!")
    return 1
</code>
the code fails with the following error message:
<code>Traceback (most recent call last):
  File "p2.py", line 10, in &lt;module&gt;
    dct2["foo"]()
TypeError: 'int' object is not callable
</code>
I am confused by this error message because <code>fun</code> was defined as a function, not an integer.


A:

The problem is that <code>fun</code> from <code>p1.py</code> is no longer a function after pickle/
