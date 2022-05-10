import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return []
class A(object):
    pass
a = A()
a.__add__ = fun
a + a
</code>
Which works fine on Python 2.7, but here is how it behaves on Python 3.3 :
<code>Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 01:25:11) [MSC v.1600 32 bit (Intel)] on win32   
Type "copyright", "credits" or "license()" for more information.  
&gt;&gt;&gt; import ctypes  
&gt;&gt;&gt; FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)  
&gt;&gt;&gt; @FUNTYPE  
... def fun():  
...     return []  
...  
&gt;&gt;&gt; class A(object):  
...     pass  
...  
&gt;&gt;&gt; a = A()  
&gt;&gt;&gt; a.__add__ =
