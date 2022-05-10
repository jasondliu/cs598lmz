import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def test(s):
    print(s.x)
    print(s.y)

s = S()
test(s)
</code>
This gives me the following error:
<code>Traceback (most recent call last):
  File "C:\Users\Jelle\Documents\GitHub\ctypes_test\ctypes_test.py", line 13, in &lt;module&gt;
    test(s)
  File "C:\Users\Jelle\Documents\GitHub\ctypes_test\ctypes_test.py", line 6, in test
    print(s.x)
AttributeError: 'S' object has no attribute 'x'
</code>
What am I doing wrong?


A:

<code>S.x</code> is a class attribute, not an instance attribute.  You need to call <code>S()</code> to create an instance of the class.  You can then access the instance attributes. 

