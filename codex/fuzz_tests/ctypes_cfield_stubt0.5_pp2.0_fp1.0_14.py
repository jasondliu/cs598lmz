import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyField(ctypes.CField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_field = True

class MyStructure(ctypes.Structure):
    _fields_ = [('x', MyField(ctypes.c_int))]

print(MyStructure.x.my_field)
</code>
This works fine with Python 3.7.2, but fails with Python 3.6.8 with the error:
<code>Traceback (most recent call last):
  File "/home/me/test.py", line 13, in &lt;module&gt;
    print(MyStructure.x.my_field)
AttributeError: 'MyField' object has no attribute 'my_field'
</code>
I'm not sure what's going on here.  I don't see any relevant changes in the ctypes source between 3.6.8 and 3.7.2.  What is Python 3.6.8 doing differently?


A:

The
