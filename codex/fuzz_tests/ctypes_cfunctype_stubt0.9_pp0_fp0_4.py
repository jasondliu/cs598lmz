import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print "hello, i am a function returned by a function"
    return 0

def function_returning_function():
    print "returning function"
    return fun

def function_accepting_function(f):
    print "accepted function from python"
    return f()
</code>
However this code causes a stackoverflow in CPython (I assume other implementations would behave similarly)
<code>&gt;&gt;&gt; import mod
returning function
accepted function from python
hello, i am a function returned by a function
hello, i am a function returned by a function
hello, i am a function returned by a function
hello, i am a function returned by a function
hello, i am a function returned by a function
hello, i am a function returned by a function
hello, i am a function returned by a function
hello, i am a function returned by a function
hello, i am a function returned by a function
hello, i am a function returned by a function
hello, i am a function returned by a function
hello, i am a function returned by a function
hello, i am a
