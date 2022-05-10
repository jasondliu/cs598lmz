import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def dummy(x):
    return x

def main():
    f = FUNTYPE(dummy)
    f(2)

main()
</code>
I get the following error:
<code>Traceback (most recent call last):
File "test.py", line 12, in &lt;module&gt;
main()
File "test.py", line 9, in main
f(2)
TypeError: 'int' object is not callable
</code>
What is the problem?


A:

The problem is that you are trying to call an integer as a function.  <code>f</code> is a function pointer, but <code>FUNTYPE</code> returns an integer.  You need to change the return type of <code>FUNTYPE</code> to be <code>ctypes.c_void_p</code> and then cast it to a function pointer.  Then you can call <code>f</code>.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
