import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)
    y = ctypes.c_int(1)

s = S()

print s.x
print s.y

s.x = 2

print s.x
print s.y

s.y = 3

print s.x
print s.y

s.x = 4

print s.x
print s.y
</code>
Output:
<code>0
1
2
1
2
3
4
3
</code>
Why does this happen?


A:

The important part of the documentation is this:
<blockquote>
<p>If an instance attribute with the same name as a field is defined, it hides the field.</p>
</blockquote>
When you set <code>s.x = 2</code>, you're not modifying the <code>x</code> field of the <code>S</code> structure; you're setting an instance attribute on the <code>s</code> instance.  This is the same as if you had done <code>s.x = 2</code
