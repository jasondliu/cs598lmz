import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.FieldType = type(int)
class SField(ctypes.Structure):
    _fields_ = [("S", ctypes.c_int),("Q", ctypes.c_int)]
ctypes.SubFieldType = type(SField.S)
</code>
<code>type(SField.S)</code> is not the same as <code>type(ctypes.c_int)</code>.
The question is: How does <code>ctypes.Fieldtype</code> actually instatiate? When I tried to do something like <code>ctypes.FieldType(11)</code>, it raised a <code>TypeError</code>, stating <code>'FieldType' object is not callable. How should I instatiate this class?</code>


A:

Trying to create an instance of <code>ctypes.FieldType</code> is not meaningful; you do that by creating an instance of its (one and only) subclass, <code>ctypes.CField</code>, by passing an <code>ctypes</code> data type to it.

