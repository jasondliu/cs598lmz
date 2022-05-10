import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

def main():
    ctypes.pointer(C())

main()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "C:\Users\josh\Documents\Python\ctypes_test.py", line 13, in &lt;module&gt;
    main()
  File "C:\Users\josh\Documents\Python\ctypes_test.py", line 10, in main
    ctypes.pointer(C())
  File "C:\Python27\lib\ctypes\__init__.py", line 558, in __init__
    self._length_ = len(self._type_._fields_)
TypeError: object of type 'CField' has no len()
</code>
I'm not sure why this is happening. I can't find any reference to the <code>CField</code> type in the <code>ctypes</code> module.
Am I doing something wrong, or is this
