import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())
</code>
This works fine. But if I change the function to something like this:
<code>@FUNTYPE
def fun(a):
    return 42
</code>
I get an error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    print(fun())
TypeError: fun() takes exactly 1 argument (0 given)
</code>
This is not a problem of the <code>print</code> function, but of the <code>fun</code> function itself.
Why does this happen?


A:

In the first example, you are not passing any arguments to the function. In the second example, you are passing no arguments to the function.
In the first example, the <code>fun</code> function is declared to take no arguments. In the second example, the <code>fun</code> function is declared to take one argument.
When you call <code>fun()</code>, you are not passing any arguments. But the <code>fun</code> function
