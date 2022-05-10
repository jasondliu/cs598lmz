import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

foo = S()
print(foo.x, foo.y)
foo.z = ctypes.c_int(3)
print(foo.x, foo.y, foo.z)
</code>
This prints:
<code>1 2
1 2 3
</code>
But when I try to create a new class <code>S2</code> that inherits from <code>S</code> and try to define the same variable <code>z</code>, I get an error:
<code>class S2(S):
    z = ctypes.c_int(3)

foo2 = S2()
print(foo2.x, foo2.y, foo2.z)
</code>
<blockquote>
<p>TypeError: <strong>init</strong>() got multiple values for argument 'x'</p>
</blockquote>
Is there a way to define members in the subclass?


A:

The problem is that you are passing <code>
