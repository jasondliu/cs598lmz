import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print "this is a test"
print fun()

print "this is a test"
print fun()

print "this is a test"
print fun()

print "this is a test"
print fun()

print "this is a test"
print fun()
</code>
and the output
<code>this is a test
hello
this is a test
hello
this is a test
hello
this is a test
hello
this is a test
hello
</code>
So it seems like this is a bug in ctypes, or maybe I'm doing something wrong.  Any suggestions?

