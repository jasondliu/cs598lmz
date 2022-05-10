import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

print fun()

def fun2():
    return 'hello'
print fun2()
</code>
I get the following output:
<code>&lt;__main__.FUNTYPE object at 0x7f6a7f1e9c10&gt;
hello
</code>
I am using Python 2.7.
Can someone explain to me why this is happening?


A:

<code>ctypes.CFUNCTYPE</code> is a function that creates a class.  You are printing the class itself, not an instance of the class.  You need to call the class to create an instance of it:
<code>print FUNTYPE()
</code>

