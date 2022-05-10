import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.__c_field = None

    @property
    def c_field(self):
        return self.__c_field

    @c_field.setter
    def c_field(self, value):
        if not isinstance(value, ctypes.CField):
            raise TypeError("c_field must be a ctypes.CField")
        self.__c_field = value


c = C()
c.c_field = S.x
print(c.c_field)

c.c_field = "foobar"
</code>
This code raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 29, in &lt;module&gt;
    c.c_field = "foobar"
  File "test.py", line 23, in c_field
    raise TypeError("c_field must be a ctypes.CField")
TypeError: c_field must be a ctypes.CField
</code>
