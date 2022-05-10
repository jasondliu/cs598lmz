import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()

class A(ctypes.Structure):
    _fields_ = [('s', S)]

class B(ctypes.Structure):
    _fields_ = [('s', S)]

class C(ctypes.Structure):
    _fields_ = [('a', A), ('b', B)]

c = C()
c.a.s.x = 1
c.b.s.x = 2

print c.a.s.x
print c.b.s.x

print c.a.s
print c.b.s
</code>
prints the following:
<code>2
2
&lt;__main__.S object at 0x1004e3b10&gt;
&lt;__main__.S object at 0x1004e3b10&gt;
</code>
Is there any way to get it to print out the actual values of the S instances, instead of just the addresses?


A:

<code>print c.a.s
print c.b.s
</code
