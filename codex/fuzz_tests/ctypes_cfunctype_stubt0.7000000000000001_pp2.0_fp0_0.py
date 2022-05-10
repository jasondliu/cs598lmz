import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello world."

fun()
</code>
On a unix box this returns
<code>'Hello world.'
</code>
On Windows XP I get an exception:
<code>Traceback (most recent call last):
  File "C:\cygwin\home\me\.\test.py", line 9, in &lt;module&gt;
    fun()
WindowsError: exception: access violation writing 0x00B50018
</code>
I've tried using <code>ctypes.c_char_p</code> instead of <code>ctypes.py_object</code> but that seems to kill it on unix as well.
Any ideas?


A:

The <code>ctypes</code> API has a <code>CFUNCTYPE</code> method for each type of return value.  You need to use <code>CFUNCTYPE(ctypes.c_char_p)</code> for the function type:
<code>from ctypes import *

def fun():
    return "Hello world."

FUNTYPE = CFUNCTY
