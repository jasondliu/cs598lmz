import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

print(fun())
</code>
this program is from the python doc
https://docs.python.org/3/library/ctypes.html#passing-callback-functions-as-arguments
the result is as below
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    print(fun())
TypeError: calling a function pointer with invalid signature
</code>
The python version I used is 
<code>Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
</code>
And the os is ubuntu 16.04.
Is there something wrong in my code? thanks for help


A:

Thanks for the answer and help of @eryksun
The solution like this
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
@FUNTYPE
def fun():
    return b'hello'

print(fun
