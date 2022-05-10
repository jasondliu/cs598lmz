import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(n):
    print "my_callback", n
    return n

my_callback_c = FUNTYPE(my_callback)
lib.my_callback = my_callback_c

lib.my_callback(4)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    lib.my_callback = my_callback_c
TypeError: in method 'my_callback', argument 1 of type 'int (*)(int)'
</code>
I have tried a few different things, but I can't figure out what I'm doing wrong.


A:

You are using <code>ctypes</code> wrong.  <code>my_callback_c</code> is a function with a <code>ctypes</code> type.  You should be passing that function to the C function, not assigning it to a C function.
<code>lib.my_function(my_callback_
