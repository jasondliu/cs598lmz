import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    pass

def main():
    s = S()
    c = C()
    c.x = 1
    s.x = 1
    print(s.x)

main()
</code>
The code above will run without any problem, but when I change <code>ctypes.CField = type(S.x)</code> to <code>ctypes.CField = type(C.x)</code>, it will throw an error:
<code>Traceback (most recent call last):
  File "C:\Users\Fang\Desktop\test.py", line 13, in &lt;module&gt;
    main()
  File "C:\Users\Fang\Desktop\test.py", line 10, in main
    s.x = 1
AttributeError: 'S' object has no attribute 'x'
</code>
I don't understand why it happen. What is the difference between <code>C.x</code> and <code>S.x</code>?


A:

<code>S.x</code> is defined
